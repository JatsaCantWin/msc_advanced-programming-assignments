import java.io.IOException;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;

public class TriangleServlet extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        int x1 = Integer.parseInt(request.getParameter("x1"));
        int y1 = Integer.parseInt(request.getParameter("y1"));
        int x2 = Integer.parseInt(request.getParameter("x2"));
        int y2 = Integer.parseInt(request.getParameter("y2"));
        int x3 = Integer.parseInt(request.getParameter("x3"));
        int y3 = Integer.parseInt(request.getParameter("y3"));

        double side1 = Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
        double side2 = Math.sqrt(Math.pow((x3 - x2), 2) + Math.pow((y3 - y2), 2));
        double side3 = Math.sqrt(Math.pow((x1 - x3), 2) + Math.pow((y1 - y3), 2));

        double s = (side1 + side2 + side3) / 2;
        double area = Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));

        request.setAttribute("s", s);
        request.setAttribute("side1", side1);
        request.setAttribute("side2", side2);
        request.setAttribute("side3", side3);
        request.setAttribute("area", area);

        RequestDispatcher rd = request.getRequestDispatcher("result.jsp");
        rd.forward(request, response);
    }
}