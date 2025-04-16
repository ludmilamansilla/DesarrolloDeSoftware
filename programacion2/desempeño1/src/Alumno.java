public class Alumno {
    
    private String legajo; // Identificador del alumno.
    private String nombre; // Nombre del alumno.
    private String[] materias; // Array que contiene las materias que cursa el alumno.
    private int[] notas; // Array que contiene las notas del alumno en cada materia.

    // Constructor que inicializa los atributos del alumno.
    public Alumno(String legajo, String nombre, String[] materias, int[] notas){
        this.legajo = legajo;
        this.nombre = nombre;
        this.materias = materias;
        this.notas = notas;
    }

    // Método que devuelve el nombre del alumno.
    public String datoNombre(){
        return nombre;
    }

    // Método que devuelve el array de materias del alumno.
    public String[] datoMaterias() {
        return materias;
    }

    // Método que devuelve el array de notas del alumno.
    public int[] datoNotas() {
        return notas;
    }

    // Método que muestra el estado de las materias (Aprobada/Reprobada) según la nota de aprobación.
    public void estadoMaterias(int notaAprobacion){
        for(int i=0 ; i< materias.length ; i++){
            String condicion;
            if (notas[i] >= notaAprobacion){
               condicion = "APROBADA";
            } else {
                condicion = "REPROBADA";
            }
            System.out.println(materias[i] + ": " + condicion);
        }
    }

    // Método que calcula y retorna el promedio de las notas del alumno.
    public double promedio(){
        int suma = 0;
        for(int i=0 ; i<notas.length ; i++){
            suma += notas[i];
        }
        return (double) suma / notas.length;
    }

    // Método que muestra las materias con notas por encima del promedio del alumno.
    public void arribaDelPromedio(double promedio){
        System.out.println("Las materias de " + nombre + " por arriba del promedio son: ");
        for(int i=0 ; i<materias.length ; i++){
            if (notas[i] > promedio) {
                System.out.println(materias[i] + ": " + notas[i]);
            }
        }
    }

}