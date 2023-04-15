public class Main {
    public static void main(String[] args) {
        MockClientView view = new MockClientView();

        view.addAContact("1", "Piotr", "Jurek");
        view.addAContact("2", "Otrip", "Rekuj");
        view.addAContact("3", "Jan", "Kowalski");

        view.displayFirstLast("1");
        view.displayFirstLast("2");
        view.displayFirstLast("3");
    }
}
