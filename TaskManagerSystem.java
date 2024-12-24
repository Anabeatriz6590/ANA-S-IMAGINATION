import java.time.LocalDate;
import java.util.*;

public class TaskManagerSystem {

    private static final Scanner scanner = new Scanner(System.in);
    private static final Map<String, String> users = new HashMap<>();
    private static final Map<String, List<Task>> userTasks = new HashMap<>();
    private static final Map<String, List<Task>> completedTasks = new HashMap<>();

    public static void main(String[] args) {
        System.out.println("-------- Welcome to Task Manager --------");

        boolean authenticated = false;
        String userEmail = "";

        while (!authenticated) {
            System.out.println("1. Login");
            System.out.println("2. Register");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine();

            if (option == 1) {
                System.out.print("E-mail: ");
                String email = scanner.nextLine();
                System.out.print("Password: ");
                String password = scanner.nextLine();

                if (users.containsKey(email) && users.get(email).equals(password)) {
                    authenticated = true;
                    userEmail = email;
                    System.out.println("Login successful! Welcome, " + email);
                } else {
                    System.out.println("Incorrect email or password. Try again...");
                }
            } else if (option == 2) {
                System.out.print("E-mail: ");
                String email = scanner.nextLine();
                System.out.print("Password: ");
                String password = scanner.nextLine();

                if (users.containsKey(email)) {
                    System.out.println("Already registered user.");
                } else {
                    users.put(email, password);
                    userTasks.put(email, new ArrayList<>());
                    completedTasks.put(email, new ArrayList<>());
                    System.out.println("User registered successfully.");
                }
            } else {
                System.out.println("Invalid option. Please try again.");
            }
        }

        mainMenu(userEmail);
    }

    private static void mainMenu(String userEmail) {
        boolean running = true;

        while (running) {
            System.out.println("\n-------- Main Menu --------");
            System.out.println("1. Add task");
            System.out.println("2. View tasks");
            System.out.println("3. Delete task");
            System.out.println("4. Mark task as completed");
            System.out.println("5. View completed tasks");
            System.out.println("6. Sort tasks by due date");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");

            int option = scanner.nextInt();
            scanner.nextLine();

            switch (option) {
                case 1 -> createTask(userEmail);
                case 2 -> listTasks(userEmail);
                case 3 -> deleteTask(userEmail);
                case 4 -> markTaskAsCompleted(userEmail);
                case 5 -> viewCompletedTasks(userEmail);
                case 6 -> sortTasksByDueDate(userEmail);
                case 7 -> {
                    running = false;
                    System.out.println("Exiting the system... See you later!");
                }
                default -> System.out.println("Invalid option. Please try again.");
            }
        }
    }

    private static void createTask(String userEmail) {
        System.out.print("Task Title: ");
        String title = scanner.nextLine();
        System.out.print("Task Description: ");
        String description = scanner.nextLine();
        System.out.print("Deadline (yyyy-mm-dd): ");
        String deadlineInput = scanner.nextLine();
        LocalDate deadline = LocalDate.parse(deadlineInput);
        System.out.print("Priority (Low, Medium, High): ");
        String priority = scanner.nextLine();

        Task newTask = new Task(title, description, deadline, priority);
        userTasks.get(userEmail).add(newTask);
        System.out.println("Task created successfully.");
    }

    private static void listTasks(String userEmail) {
        List<Task> tasks = userTasks.get(userEmail);
        if (tasks.isEmpty()) {
            System.out.println("No tasks found.");
        } else {
            System.out.println("\n-------- Your Tasks --------");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    private static void deleteTask(String userEmail) {
        List<Task> tasks = userTasks.get(userEmail);
        if (tasks.isEmpty()) {
            System.out.println("No tasks to delete.");
        } else {
            listTasks(userEmail);
            System.out.print("Enter the task number to delete: ");
            int taskNumber = scanner.nextInt();
            scanner.nextLine();
            if (taskNumber > 0 && taskNumber <= tasks.size()) {
                tasks.remove(taskNumber - 1);
                System.out.println("Task deleted successfully.");
            } else {
                System.out.println("Invalid number.");
            }
        }
    }

    private static void markTaskAsCompleted(String userEmail) {
        List<Task> tasks = userTasks.get(userEmail);
        if (tasks.isEmpty()) {
            System.out.println("No tasks to mark as complete.");
        } else {
            listTasks(userEmail);
            System.out.print("Enter the task number to mark as complete: ");
            int taskNumber = scanner.nextInt();
            scanner.nextLine();
            if (taskNumber > 0 && taskNumber <= tasks.size()) {
                Task completedTask = tasks.remove(taskNumber - 1);
                completedTasks.get(userEmail).add(completedTask);
                System.out.println("Task marked as complete.");
            } else {
                System.out.println("Invalid number.");
            }
        }
    }

    private static void viewCompletedTasks(String userEmail) {
        List<Task> tasks = completedTasks.get(userEmail);
        if (tasks.isEmpty()) {
            System.out.println("No completed tasks found.");
        } else {
            System.out.println("\n-------- Completed Tasks --------");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    private static void sortTasksByDueDate(String userEmail) {
        List<Task> tasks = userTasks.get(userEmail);
        if (tasks.isEmpty()) {
            System.out.println("No tasks to order.");
        } else {
            tasks.sort(Comparator.comparing(Task::getDeadline));
            System.out.println("Tasks ordered by deadline: ");
            listTasks(userEmail);
        }
    }
}

class Task {
    private final String title;
    private final String description;
    private final LocalDate deadline;
    private final String priority;

    public Task(String title, String description, LocalDate deadline, String priority) {
        this.title = title;
        this.description = description;
        this.deadline = deadline;
        this.priority = priority;
    }

    public LocalDate getDeadline() {
        return deadline;
    }

    @Override
    public String toString() {
        return "Title: " + title + ", Description: " + description + ", Deadline: " + deadline + ", Priority: " + priority;
    }
}
