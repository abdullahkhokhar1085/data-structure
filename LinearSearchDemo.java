import java.util.Scanner;

public class LinearSearchDemo {
    private int n;
    private int[] data;
    private int size;

    public LinearSearchDemo(int size) {
        this.size = size;
        this.data = new int[size];
    }

    public int linearSearch(int target) {
        for (int j = 0; j < n; j++) {
            if (target == data[j]) {
                return j + 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the NUV");
        LinearSearchDemo ls = new LinearSearchDemo(100);

        System.out.print("Enter how many elements do you want to enter? : ");
        ls.n = scanner.nextInt();

        if (ls.n > ls.size) {
            System.out.println("Array size is not supporting");
        } else {
            for (int i = 0; i < ls.n; i++) {
                System.out.print("Enter value: ");
                int value = scanner.nextInt();
                ls.data[i] = value;
            }

            System.out.println("Values available in the Array");
        }

        System.out.print("Enter value to find: ");
        int target = scanner.nextInt();

        // Function Call
        int isAvailable = ls.linearSearch(target);

        // Checking return value
        if (isAvailable == 0) {
            System.out.println("Entered value is not available in the given Array");
        } else {
            System.out.println("Entered value is available at position " + isAvailable);
        }
        scanner.close();
    }
}