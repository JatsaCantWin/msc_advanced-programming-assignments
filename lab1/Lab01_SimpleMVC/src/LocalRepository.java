import java.util.HashMap;

public class LocalRepository {
    public static HashMap<String, Contact> contacts = new HashMap<>();

    public static void addAContact(String id, String name, String last_name)
    {
        Contact newContact = new Contact(id, name, last_name);
        contacts.put(id, newContact);
    }

    public static Contact getContact(String id)
    {
        return contacts.get(id);
    }

    public static void displayFirstLast(String contactID)
    {
        System.out.println(contacts.get(contactID).toString());
    }
}