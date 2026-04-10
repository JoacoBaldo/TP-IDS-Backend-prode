# TP-IDS-Backend-prode
Sistema Backend completo para un servicio de apuestas deportivas online similar al Prode

## Configuración Rápida con Docker MySQL

### Prerrequisitos
- Docker Desktop instalado
- Git clonado del proyecto

### Iniciar Base de Datos
```bash
# En la raíz del proyecto
docker-compose up -d
```

Esto iniciará:
- MySQL en `localhost:3306`
- phpMyAdmin en `http://localhost:8080` (opcional)

### Configurar Variables de Entorno
```bash
# Copiar el archivo de configuración
cp .env.docker .env
```

### Iniciar Aplicación
```bash
cd Prode/src
python app.py
```

La aplicación estará en `http://localhost:5000`

### Estructura de la Base de Datos
- `users` - Usuarios del sistema
- `fixtures` - Partidos/Encuentros
- `predictions` - Predicciones de los usuarios
- `rankings` - Tabla de posiciones

### Datos de Ejemplo
El sistema incluye datos de ejemplo de la Copa América 2024:
- 4 usuarios de prueba
- 6 partidos de ejemplo
- Predicciones de ejemplo

### Comandos Útiles
```bash
# Ver logs de MySQL
docker-compose logs mysql

# Detener servicios
docker-compose down

# Reiniciar base de datos (elimina datos)
docker-compose down -v
docker-compose up -d
```

---

### Contexto
Con la inminente llegada de la Copa Mundial de la FIFA 2026, la fiebre futbolística vuelve
a apoderarse de la sociedad argentina. En un país donde el fútbol trasciende lo deportivo para
consolidarse como un pilar de la identidad y la cultura nacional, ahora potenciado por el orgullo
de defender el título, las viejas y nuevas tradiciones convergen. El clásico ritual de completar
el fixture partido a partido y la histórica organización del prode en oficinas, escuelas y grupos de
amigos siguen más vigentes que nunca.

### ¿Que es un Fixture?
Un fixture es la planificacion completa de los partidos de un torneo. Define:
Que equipos se enfrentan
En que fecha
En que instancia del torneo

### ¿Que es un ProDe?
El ProDe (Pronosticos Deportivos) es un sistema donde los usuarios predicen resultados
de partidos.

## Enunciado
Una empresa tecnologica, con el objetivo de fomentar el compa˜nerismo, la participacion y la
interaccion entre sus colaboradores, solicita a un equipo de desarrollo la implementacion de una
aplicacion tipo “prode” con motivo del Mundial.
La iniciativa tendra ademas un caracter solidario: para participar, cada empleado debera colaborar
con un alimento no perecedero. Como incentivo adicional, se premiara a los cinco participantes que
obtengan las mejores posiciones en el ranking final.
El trabajo de hacer esta app estara destinado a distintos equipos que se encargaran, entre otras
cosas, de hacer el Frontend y otros servicios.
A tu equipo se le pide en particular desarrollar una API backend que permita gestionar el fixture
del Mundial de Futbol 2026.


### La solucion debera permitir:
Construir y administrar un fixture de partidos.
Registrar encuentros indicando:
- Equipo local
- Equipo visitante
- Estadio
- Ciudad
- Fecha
- Fase del Torneo

### Actualizar los resultados una vez finalizados los partidos.
Consultar partidos mediante distintos criterios:
- Equipo
Pagina 3 de 9
Proyecto Backend
Introduccion al Desarrollo de Software
- Fecha
- Fase del Torneo
Implementar paginacion en los listados