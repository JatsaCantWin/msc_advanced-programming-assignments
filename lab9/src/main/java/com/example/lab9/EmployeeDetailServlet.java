package com.example.lab9;

import com.example.lab9.models.Employee;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(name = "EmployeeDetailServlet", value = "/employees/html/details")
public class EmployeeDetailServlet extends HttpServlet {
    private EntityManagerFactory entityManagerFactory;

    @Override
    public void init() throws ServletException {
        entityManagerFactory = Persistence.createEntityManagerFactory("default");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String employeeId = request.getParameter("id");

        EntityManager entityManager = entityManagerFactory.createEntityManager();

        Employee employee = entityManager.find(Employee.class, employeeId);

        if (employee != null) {
            StringBuilder htmlBuilder = new StringBuilder();
            htmlBuilder.append("<html><body>")
                    .append("<h2>Employee Details</h2>")
                    .append("<form method=\"POST\" action=\"/lab9-1.0-SNAPSHOT/employees/html/details?id=").append(employee.getId()).append("\">")
                    .append("<label>Name: <input type=\"text\" name=\"name\" value=\"").append(employee.getName()).append("\"></label><br>")
                    .append("<label>Surname: <input type=\"text\" name=\"surname\" value=\"").append(employee.getSurname()).append("\"></label><br>")
                    .append("<label>Role: <input type=\"text\" name=\"role\" value=\"").append(employee.getRole()).append("\"></label><br>")
                    .append("<input type=\"submit\" value=\"Save\">")
                    .append("</form>")
                    .append("</body></html>");

            response.setStatus(HttpServletResponse.SC_OK);
            response.setContentType("text/html");

            response.getWriter().write(htmlBuilder.toString());
        } else {
            throw new ServletException("Employee not found");
        }

        entityManager.close();
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String employeeId = request.getParameter("id");
        String name = request.getParameter("name");
        String surname = request.getParameter("surname");
        String role = request.getParameter("role");

        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();

        Employee employee = entityManager.find(Employee.class, employeeId);

        if (employee != null) {
            employee.setName(name);
            employee.setSurname(surname);
            employee.setRole(role);
        } else {
            throw new ServletException("Employee not found");
        }

        entityManager.getTransaction().commit();
        entityManager.close();

        response.sendRedirect("/lab9-1.0-SNAPSHOT/employees/html/details?id=" + employeeId);
    }

    @Override
    public void destroy() {
        if (entityManagerFactory != null) {
            entityManagerFactory.close();
        }
    }
}
