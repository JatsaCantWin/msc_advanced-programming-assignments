public class Contact {
    Long id;
    String first_name;
    String last_name;

    public Contact(String id, String first_name, String last_name) {
        this.id = Long.valueOf(id);
        this.first_name = first_name;
        this.last_name = last_name;
    }

    public String toString() {
        return id + " " + first_name + " " + last_name;
    }
}
