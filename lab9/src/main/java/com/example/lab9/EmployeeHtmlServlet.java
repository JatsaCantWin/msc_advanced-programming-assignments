package com.example.lab9;

import com.example.lab9.models.Employee;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import jakarta.persistence.TypedQuery;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;
import java.util.UUID;

@WebServlet(name = "EmployeeHtmlServlet", value = "/employees/html")
public class EmployeeHtmlServlet extends HttpServlet {
    private EntityManagerFactory entityManagerFactory;

    @Override
    public void init() throws ServletException {
        entityManagerFactory = Persistence.createEntityManagerFactory("default");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        EntityManager entityManager = entityManagerFactory.createEntityManager();

        TypedQuery<Employee> query = entityManager.createQuery("SELECT e FROM Employee e", Employee.class);
        List<Employee> employees = query.getResultList();

        StringBuilder htmlBuilder = new StringBuilder();
        htmlBuilder.append("<html><body>");

        for (Employee employee : employees) {
            htmlBuilder.append("<p>")
                    .append("<a href=\"/lab9-1.0-SNAPSHOT/employees/html/details?id=").append(employee.getId()).append("\">")
                    .append(employee.getName()).append(" ").append(employee.getSurname())
                    .append("</a>")
                    .append("</p>");
        }

        htmlBuilder.append("<h2>Add New Employee</h2>")
                .append("<form method=\"POST\" action=\"/lab9-1.0-SNAPSHOT/employees/html\">")
                .append("<label>Name: <input type=\"text\" name=\"name\"></label><br>")
                .append("<label>Surname: <input type=\"text\" name=\"surname\"></label><br>")
                .append("<label>Role: <input type=\"text\" name=\"role\"></label><br>")
                .append("<input type=\"submit\" value=\"Add\">")
                .append("</form>");

        htmlBuilder.append("</body></html>");

        response.setStatus(HttpServletResponse.SC_OK);
        response.setContentType("text/html");

        response.getWriter().write(htmlBuilder.toString());
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String surname = request.getParameter("surname");
        String role = request.getParameter("role");

        String id = UUID.randomUUID().toString();

        Employee employee = new Employee(id, name, surname, role);

        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        entityManager.persist(employee);
        entityManager.getTransaction().commit();
        entityManager.close();

        response.sendRedirect("/lab9-1.0-SNAPSHOT/employees/html");
    }

    @Override
    public void destroy() {
        if (entityManagerFactory != null) {
            entityManagerFactory.close();
        }
    }
}