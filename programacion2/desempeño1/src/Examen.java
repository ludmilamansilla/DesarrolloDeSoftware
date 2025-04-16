import java.util.Scanner;

public class Examen {

    protected Alumno[] alumnos; // Array que contiene los objetos Alumno.
    protected int notaAprobacion; // Variable que almacena la nota mínima de aprobación.


    // Constructor que inicializa el array de alumnos y la nota de aprobación.
    public Examen(Alumno[] alumnos, int notaAprobacion) {
        this.alumnos = alumnos;
        this.notaAprobacion = notaAprobacion;
    }

    // Método que muestra todos los alumnos y su estado en cada materia.
    public void mostrarAlumnos() {
        for (int i = 0; i < alumnos.length; i++) {
            Alumno alumno = alumnos[i];
            System.out.println("Alumno: " + alumno.datoNombre());
            alumno.estadoMaterias(notaAprobacion);
            System.out.println("Promedio: " + alumno.promedio());
            System.out.println();
        }
    }

     // Método que muestra las materias que están por encima del promedio de cada alumno.
    public void alumnosArribaPromedio() {
        for (int i = 0; i < alumnos.length; i++) {
            Alumno alumno = alumnos[i];
            double promedio = alumno.promedio();
            alumno.arribaDelPromedio(promedio);
        }
    }

    // Método principal que inicia la ejecución del programa.
    public static void main(String[] args) {

        // Datos de ejemplo
        String[] materias1 = { "Matemáticas", "Computación", "Ciencias" };
        int[] notas1 = { 8, 6, 9 };
        Alumno alumno1 = new Alumno("001", "Juan Rodriguez", materias1, notas1);

        String[] materias2 = { "Matemáticas", "Computación", "Ciencias" };
        int[] notas2 = { 4, 7, 5 };
        Alumno alumno2 = new Alumno("002", "María Martinez", materias2, notas2);

        Alumno[] alumnos = { alumno1, alumno2 };

        int notaAprobacion = 6;
        Examen examen = new Examen(alumnos, notaAprobacion);

        // MENÚ

        Scanner teclado = new Scanner(System.in);
        int opcion = -1;

        while (opcion != 0) {
            System.out.println("Menú:");
            System.out.println("1. Mostrar listado de alumnos");
            System.out.println("2. Mostrar materias por encima del promedio");
            System.out.println("0. Salir");

            System.out.print("Selecciona una opción: ");
            opcion = teclado.nextInt(); 

            switch (opcion) {
                case 1:
                    examen.mostrarAlumnos();
                    break;
                case 2:
                    examen.alumnosArribaPromedio();
                    break;
                case 0:
                    System.out.println("Saliendo del menú...");
                    break;
                default:
                    System.out.println("Opción inválida");
            }
        }

        teclado.close(); 
    }

}
