import javax.naming.ldap.Control;

public class MockClientView {
    Controller controller = new Controller();

    public void displayFirstLast(String id) {
        System.out.println(controller.findAContact(id));
    }
    public void addAContact(String id, String name, String last_name) {
        controller.addAContact(id, name, last_name);
    }
}
