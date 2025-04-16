package org.example;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Biblioteca {
    private Map<String, Libro> libros;

    public Biblioteca() {
        this.libros = new HashMap<>();
    }

    public void agregarLibro(Libro libro) throws IllegalArgumentException {
        if (libros.containsKey(libro.getIsbn())) {
            throw new IllegalArgumentException("El libro con ISBN " + libro.getIsbn() + " ya existe.");
        }
        libros.put(libro.getIsbn(), libro);
    }

    public Libro buscarLibroPorISBN(String isbn) {
        return libros.get(isbn);
    }

    public List<Libro> buscarLibrosPorAutor(String autor) {
        List<Libro> resultado = new ArrayList<>();
       //TODO Agregar lógica
       for (Libro libro : libros.values()) {
            if (libro.getAutor().equalsIgnoreCase(autor)) {
                resultado.add(libro);
            }
        }
        return resultado;
    }

    public List<Libro> listarTodosLosLibros() {
        return new ArrayList<>(libros.values());
    }

    public void cargarLibrosDesdeCSV(String nombreArchivo) throws IOException {
        // TODO Agregar Lógica
        // usar metodo  agregarLibro()
        try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] datos = linea.split(",");
                if (datos.length == 4) {
                    String titulo = datos[0];
                    String autor = datos[1];
                    int añoPublicacion = Integer.parseInt(datos[2].trim());
                    String isbn = datos[3].trim();
                    agregarLibro(new Libro(titulo, autor, añoPublicacion, isbn));
                }
            }
        } catch (IOException e) {
            throw new IOException("Error al leer el archivo CSV.", e);
        } catch (IllegalArgumentException e) {
            System.out.println("Advertencia: " + e.getMessage());
        }

    }

    public void guardarLibrosEnCSV(String nombreArchivo) throws IOException {
        // TODO Agregar Lógica
        // el archivo debe contener: Titulo, Autor, Año de Publicacion, ISBN
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(nombreArchivo))) {
            for (Libro libro : libros.values()) {
                bw.write(libro.getTitulo() + "," + libro.getAutor() + "," +
                        libro.getAñoPublicacion() + "," + libro.getIsbn());
                bw.newLine();
            }
        } catch (IOException e) {
            throw new IOException("Error al escribir en el archivo CSV.", e);
        }
    
    }
}
