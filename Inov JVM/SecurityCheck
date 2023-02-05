import java.sql.*;
import java.util.Objects;
import java.util.Scanner;


// Security Functions for accounts.

public class SecurityCheck {

    public static Connection connect() {
        try {
            Class.forName("org.postgresql.Driver");
            Connection connection = DriverManager.getConnection("jdbc:postgresql://localhost/inovjava", "postgres", "");
            System.out.println("Connecting to network.");
            return connection;
        } catch (SQLException e) {
            throw new RuntimeException("Cannot connect to network", e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public void Login_to_Accnt() throws SQLException {
        Statement state = connect().createStatement();
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter card number:");
        int card_num = scan.nextInt();
        ResultSet check_Debit_data = state.executeQuery("SELECT CARDNUM FROM InovDEBIT WHERE CARDNUM=?");
        while (check_Debit_data.next()) {
            int Num_of_tries = 0;
            int card_num_Debit_data = check_Debit_data.getInt("CARDNUM");
                if (card_num == card_num_Debit_data) {
                    System.out.println("Access granted");
                    // direct to main menu
                }
                else {
                    ResultSet check_Credit_data = state.executeQuery("SELECT CARDNUM FROM InovDEBIT WHERE CARDNUM=?");
                    int card_num_Credit_data = check_Credit_data.getInt("CARDNUM");
                    if (card_num == card_num_Credit_data){
                        System.out.println("Access granted");
                        // direct to main menu
                    } else {
                        int i = Num_of_tries + 1;
                        System.out.println("Try again");
                            if (Objects.equals(i, 3)) {
                                System.out.println("You have been blocked from Logging in at this moment/" +
                                    "You will recieve an email on how to fix this shortly.");
                                //email
                                break;
                            }
                    }
                }
        }
    }
   // Process to secure account if blocked from Login.
   // starts with selection of account type.
    public void Secure_Account(){
        Scanner scan = new Scanner(System.in);
        System.out.println("1. Debit:");
        System.out.println("2. Credit:");
        String Accnt_type = scan.nextLine();
        if (Objects.equals(Accnt_type, "1")){
            Retrieve_Account_Debit(); // get back Debit account
        } if (Objects.equals(Accnt_type, "2")){
            Retrieve_Account_Credit(); // get back Credit account
        }
    }

    public void Retrieve_Account_Debit(){

    }

    public void Retrieve_Account_Credit(){

    }
}
