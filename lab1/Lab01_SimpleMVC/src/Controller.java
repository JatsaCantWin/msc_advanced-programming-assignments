public class Controller {

    public void addAContact(String id, String name, String last_name)
    {
        LocalRepository.addAContact(id, name, last_name);
    }

    public String findAContact(String id)
    {
        return LocalRepository.getContact(id).toString();
    }
}