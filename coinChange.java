public class CoinChange {
    public static void makeChange(int n) {
        // Create a 2D array to store the unique combinations
        int[][] result = new int[1000][4];
        int count = 0;

        // Iterate over the number of quarters
        for (int quarters = 0; quarters <= n / 25; quarters++) {
            int remainingAfterQuarters = n - quarters * 25;
            // Iterate over the number of dimes
            for (int dimes = 0; dimes <= remainingAfterQuarters / 10; dimes++) {
                int remainingAfterDimes = remainingAfterQuarters - dimes * 10;
                // Iterate over the number of nickels
                for (int nickels = 0; nickels <= remainingAfterDimes / 5; nickels++) {
                    int remainingAfterNickels = remainingAfterDimes - nickels * 5;
                    // The remaining amount is the number of pennies
                    int pennies = remainingAfterNickels;

                    // Check for duplicates before adding
                    boolean isDuplicate = false;
                    for (int i = 0; i < count; i++) {
                        if (result[i][0] == quarters && result[i][1] == dimes && result[i][2] == nickels && result[i][3] == pennies) {
                            isDuplicate = true;
                            break;
                        }
                    }

                    // Add the combination if it's not a duplicate
                    if (!isDuplicate) {
                        result[count][0] = quarters;
                        result[count][1] = dimes;
                        result[count][2] = nickels;
                        result[count][3] = pennies;
                        count++;
                    }
                }
            }
        }

        // Print the results
        for (int i = 0; i < count; i++) {
            System.out.println("[" + result[i][0] + ", " + result[i][1] + ", " + result[i][2] + ", " + result[i][3] + "]");
        }
    }

    public static void main(String[] args) {
        int n = 12; // Test with different values of n
        makeChange(n);
    }
}