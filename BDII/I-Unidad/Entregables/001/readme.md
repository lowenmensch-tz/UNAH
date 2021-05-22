```
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/22
```

# Repaso 

Crear aplicación para dar solución a la problemática presentada por el maestro utilizando SQLITE, se presentará código, diagrama relacional, ejecutable (Archivo.Exe) y pequeño Instructivo. cualquier otro formato se considerara como **NO PRESENTADO**.

Se defenderá frente a toda la clase.

## Definicion del Ejercicio 

El aeropuerto *Air Canadá Center*, desea llevar un control sobre las personas que entran y salen de sus puertas para lo que requiere realizar un control.

Este control tomara los datos de las personas una tan sola vez luego a la persona se la dará un Id que ingresara en la puerta para poder abrir la puerta y salir o entrar según lo necesite.

De las personas se desea guardar la información general como ser Identificación que siempre será el numero de pasaporte que consta de 12 caracteres, los cuales pueden ser letras o números, seguidamente el nombre completo que serian dos nombres y dos apellidos, así como también el país de origen. Luego una lista de teléfonos que pueden ser de diferentes países por los cual se requiere identificar el área de cada teléfono.

El control de entradas y salida se guardará de la siguiente forma, Persona, Actividad que puede ser entrar o salir y la fecha y hora de la actividad.

Cabe mencionar que a cada persona se le identificara si es empleado o no del Aeropuerto. 

## Identificación de las reglas de negocio

### Se listan:
- Control de personas que entran y salen del aeropuerto
- Para el registro de las personas, se hará una sola vez, a partir de aquí se le dará un identificador único que ingresará cada vez que este pase por las puertas (sea que salga o entre al aeropuerto)
- **De las personas** se dea guardar: 
  - Número de pasaporte (consta de 12 carácteres alfanuméricos  )
  - Nombre completo (2 nombres, 2 apellidos)
  - País de origen
  - Tipo de persona (Empleado o cliente de la aerolínea)
  - Lista de número de teléfonos (pueden ser varios)
    - guardar el número de área o zona
- **Control de entrada/salida**
  - Actividad que realiza la persona (Entrada o salida)
  - Fechay hora de la actividad