import java.sql.*;
import java.util.Objects;
import java.util.Scanner;
import javax.crypto.KeyGenerator;
import java.security.SecureRandom;
import java.io.UnsupportedEncodingException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
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
        ResultSet check_Debit_data = state.executeQuery("SELECT CARDNUM FROM InovDebit WHERE CARDNUM=?");
        while (check_Debit_data.next()) {
            int Num_of_tries = 0;
            int card_num_Debit_data = check_Debit_data.getInt("CARDNUM");
            if (card_num == card_num_Debit_data) {
                System.out.println("Access granted");
                // direct to main menu
            } else {
                ResultSet check_Credit_data = state.executeQuery("SELECT CARDNUM FROM InovCredit WHERE CARDNUM=?");
                int card_num_Credit_data = check_Credit_data.getInt("CARDNUM");
                if (card_num == card_num_Credit_data) {
                    System.out.println("Access granted");
                    // direct to main menu
                } else {
                    int i = Num_of_tries + 1;
                    System.out.println("Try again");
                    if (Objects.equals(i, 3)) {
                        System.out.println("You have been blocked from Logging in at this moment/" +
                                "You will recieve an email on how to fix this shortly.");
                        // email notification
                        break;
                    }
                }
            }
        }
    }

    // Process to secure account if blocked from Login. (Virtual Debit & Credit) (US Only)
    // starts with selection of account type .
    public void Secure_Account(String Accnt_type, String c_code) throws SQLException, NoSuchAlgorithmException {
        if (Objects.equals(Accnt_type, "Debit")) {
            Retrieve_Account_Debit(c_code); // get back Debit account
        }
        if (Objects.equals(Accnt_type, "Credit")) {
            Retrieve_Account_Credit(c_code); // get back Credit account
        }
    }

    public void Retrieve_Account_Debit(String c_code) throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        ResultSet retrieve_Debit_data = state.executeQuery("SELECT CARDCODE FROM InovDebit WHERE CARDCODE=?");
        while (retrieve_Debit_data.next()) {
            String card_code_Debit_data = retrieve_Debit_data.getString("CARDCODE");
            if (Objects.equals(c_code, card_code_Debit_data)) {
                Login_to_Accnt();
            } else {
                recover_account_Debit();
                break;
            }
        }
    }

    public void recover_account_Debit() throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");
        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();
        //Initializing the KeyGenerator
        keyGen.init(secRandom);
        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        int card_num = secRandom.nextInt(11111);
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter name of the account holder:");
        String accnt_name = scan.nextLine();
        String retrieve_Debit_data = "UPDATE  InovDebit SET CARDNUM=?, CARDCODE=? WHERE NAME=?  ";
        PreparedStatement stat = connect().prepareStatement(retrieve_Debit_data);
        stat.setInt(1, card_num);
        stat.setString(2, get_code);
        stat.setString(2, accnt_name);
        stat.executeUpdate();
    }

    public void Retrieve_Account_Credit(String c_code) throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        ResultSet retrieve_Debit_data = state.executeQuery("SELECT CARDCODE FROM InovCredit WHERE CARDCODE=?");
        while (retrieve_Debit_data.next()) {
            String card_code_Debit_data = retrieve_Debit_data.getString("CARDCODE");
            if (Objects.equals(c_code, card_code_Debit_data)) {
                Login_to_Accnt();
            } else {
                recover_account_Credit();
                break;
            }
        }
    }
    public void recover_account_Credit() throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");
        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();
        //Initializing the KeyGenerator
        keyGen.init(secRandom);
        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        int card_num = secRandom.nextInt(11111);
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter name of the account holder:");
        String accnt_name = scan.nextLine();
        String retrieve_Debit_data = "UPDATE  InovCredit SET CARDNUM=?, CARDCODE=? WHERE NAME=?  ";
        PreparedStatement stat = connect().prepareStatement(retrieve_Debit_data);
        stat.setInt(1, card_num);
        stat.setString(2, get_code);
        stat.setString(2, accnt_name);
        stat.executeUpdate();
    }

    // Virtual International Debit Accounts
    public void International_Accnt_Login() throws SQLException {
        Statement state = connect().createStatement();
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter card number:");
        int card_num = scan.nextInt();
        ResultSet check_Debit_data = state.executeQuery("SELECT CARDNUM FROM InovInterDEBIT WHERE CARDNUM=?");
        while (check_Debit_data.next()) {
            int Num_of_tries = 0;
            int card_num_Debit_data = check_Debit_data.getInt("CARDNUM");
            if (card_num == card_num_Debit_data) {
                System.out.println("Access granted");
                // direct to main menu
            } else {
                int i = Num_of_tries + 1;
                System.out.println("Try again");
                if (Objects.equals(i, 3)) {
                    System.out.println("You have been blocked from Logging in at this moment/" +
                            "You will recieve an email on how to fix this shortly.");
                    // email notification
                    break;
                }
            }
        }
    }

    // Process to secure account if blocked from Login.
    // only one account type for International Accounts (Debit).
    public void Retrieve_International_Account_Debit(String c_code) throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        ResultSet retrieve_Debit_data = state.executeQuery("SELECT CARDCODE FROM InovInterDEBIT WHERE CARDCODE=?");
        while (retrieve_Debit_data.next()) {
            String card_code_Debit_data = retrieve_Debit_data.getString("CARDCODE");
            if (Objects.equals(c_code, card_code_Debit_data)) {
                International_Accnt_Login();
            } else {
                recover_International_Account_Debit();
                break;
            }
        }
    }

    public void recover_International_Account_Debit() throws SQLException, NoSuchAlgorithmException {
        Statement state = connect().createStatement();
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");
        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();
        //Initializing the KeyGenerator
        keyGen.init(secRandom);
        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        int card_num = secRandom.nextInt(11111);
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter name of the account holder:");
        String accnt_name = scan.nextLine();
        String retrieve_Debit_data = "UPDATE  InovInterDEBIT SET CARDNUM=?, CARDCODE=? WHERE NAME=?  ";
        PreparedStatement stat = connect().prepareStatement(retrieve_Debit_data);
        stat.setInt(1, card_num);
        stat.setString(2, get_code);
        stat.setString(2, accnt_name);
        stat.executeUpdate();
    }
}
