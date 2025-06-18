from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select, create_engine, SQLModel
from models import City, Connection

app = FastAPI()
engine = create_engine("sqlite:///cities_connections.db") 

# Create tables if they don't exist
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

@app.get("/cities")
def list_cities():
    with Session(engine) as session:
        cities = session.exec(select(City)).all()
        return cities

@app.get("/connections")
def list_connections():
    with Session(engine) as session:
        conns = session.exec(select(Connection)).all()
        return conns


@app.get("/route")
def calc_route(origin: str, destination: str):
    with Session(engine) as session:
        # Comprobar que existen ambas ciudades
        if not session.get(City, origin) or not session.get(City, destination):
            raise HTTPException(status_code=404, detail="Ciudad de origen o destino no existe")
        
        # BFS para encontrar el camino más corto
        from collections import deque

        queue = deque()
        queue.append((origin, []))  # (ciudad actual, lista de conexiones usadas)
        visited = set()

        while queue:
            current_city, path = queue.popleft()
            if current_city == destination:
             
                return {
                    "steps": [
                        {
                            "from": conn.origin,
                            "to": conn.destination,
                            "type": conn.type,
                            "plate": conn.plate,
                            "flight_number": conn.flight_number,
                            "seat": conn.seat,
                            "ship_number": conn.ship_number
                        }
                        for conn in path
                    ],
                    "cities": [origin] + [conn.destination for conn in path]
                }
            visited.add(current_city)
            # Buscar conexiones desde la ciudad actual
            conns = session.exec(
                select(Connection).where(Connection.origin == current_city)
            ).all()
            for conn in conns:
                if conn.destination not in visited:
                    queue.append((conn.destination, path + [conn]))
        # Si no hay camino
        raise HTTPException(status_code=404, detail="No existe ruta entre esas ciudades")
