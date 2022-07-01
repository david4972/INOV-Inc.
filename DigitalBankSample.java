// Example showing implementation of Inov Api

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.sql.SQLException;
import java.util.Scanner;


public class BankSample {


    public static void intro() throws NoSuchAlgorithmException, SQLException, IOException {
        Scanner scan = new Scanner(System.in);
        System.out.println("Please select what you'd like to do today?");
        System.out.println("1. create account");
        System.out.println("2. Deposit");
        System.out.println("3. Send Money");
        System.out.println("4. Currency Exchange");
        String read = scan.nextLine();
        if (read.equals("1")){
            create_accnt();
        } if (read.equals("2")){
            deposit();
        } if (read.equals("3")){
            send_money();
        } if (read.equals("4")){
            Currency_exchange();
        }
    }

    public static void create_accnt() throws NoSuchAlgorithmException {
        Scanner scan = new Scanner(System.in);
        System.out.println("Please select ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        System.out.println("3. International Debit account");
        String read = scan.nextLine();
        if (read.equals("1")) {
            create_accnt_debit();
        } if (read.equals("2")) {
            create_accnt_credit();
        } if (read.equals("3")) {
            create_International_accnt_debit();
        }
    }


    public static void deposit() throws SQLException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        //Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        Scanner scan4 = new Scanner(System.in);
        Scanner scan5 = new Scanner(System.in);
        System.out.print("Please enter virtual account number: ");
        int account_num = scan.nextInt();
        System.out.print("Please enter amount you want to deposit: ");
        double account_deposit = scan4.nextDouble();
        System.out.println("Please select ?");
        System.out.println("1. Checking");
        System.out.println("2. Saving");
        String accnt_choice = scan3.nextLine();
        System.out.println("Please select ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        String accnt_line = scan5.nextLine();
        if (accnt_choice.equals("1") && accnt_line.equals("1")){
            Inov.deposit_checking_debit(account_num, account_deposit);
        } if (accnt_choice.equals("2") && accnt_line.equals("1")){
            Inov.deposit_saving_debit(account_num, account_deposit);
        } if (accnt_choice.equals("1") && accnt_line.equals("2")){
            Inov.deposit_checking_credit(account_num, account_deposit);
        } if (accnt_choice.equals("2") && accnt_line.equals("2")){
            Inov.deposit_saving_credit(account_num, account_deposit);
        }
    }

    public static void create_accnt_debit() throws NoSuchAlgorithmException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        System.out.print("Please enter account name: ");
        String account_name = scan.nextLine();
        System.out.print("Please enter account email: ");
        String account_email = scan2.nextLine();
        System.out.print("Please enter address: ");
        String account_address = scan3.nextLine();
        Inov.create_debit_account(account_name, account_email, account_address);
    }

    public static void create_International_accnt_debit() throws NoSuchAlgorithmException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        System.out.print("Please enter account name: ");
        String account_name = scan.nextLine();
        System.out.print("Please enter account email: ");
        String account_email = scan2.nextLine();
        System.out.print("Please enter address: ");
        String account_address = scan3.nextLine();
        System.out.print("Please enter Your CountryCode, Example (USD for United States Dollar): ");
        String account_country = scan3.nextLine();
        Inov.create_International_debit_account(account_name, account_email, account_address, account_country);
    }

    public static void create_accnt_credit() throws NoSuchAlgorithmException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        System.out.print("Please enter account name: ");
        String account_name = scan.nextLine();
        System.out.print("Please enter account email: ");
        String account_email = scan2.nextLine();
        System.out.print("Please enter address: ");
        String account_address = scan3.nextLine();
        Inov.create_credit_account(account_name, account_email, account_address);
    }

    public static void send_money() throws SQLException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        Scanner scan4 = new Scanner(System.in);
        System.out.print("Will you be sending money Internationally today?: ");
        System.out.print("1. Yes ");
        System.out.print("2. No ");
        String inter_choice = scan4.nextLine();
        if (inter_choice.equals("1")) {
            send_money_internationally();
        } else {
            System.out.print("Please enter virtual account number: ");
            int account_num = scan.nextInt();
            System.out.print("Please enter name of person receiving money: ");
            String receive = scan2.nextLine();
            System.out.print("Please enter amount you want to deposit: ");
            double account_deposit = scan.nextDouble();
            System.out.println("Please select ?");
            System.out.println("1. Debit ");
            System.out.println("2. Credit ");
            String accnt_line = scan3.nextLine();
            if (accnt_line.equals("1")) {
                Inov.send_money_debit(account_num, account_deposit, receive);
            } else {
                Inov.send_money_credit(account_num, account_deposit, receive);
            }

        }
    }

    public static void send_money_internationally() throws SQLException {
         inov Inov2 = new inov();
         Scanner scan_interdebit = new Scanner(System.in);
         Scanner scan_interdebit2 = new Scanner(System.in);
         Scanner scan_interdebit3 = new Scanner(System.in);
         System.out.print("Please enter virtual account number: ");
         int account_num = scan_interdebit.nextInt();
         System.out.print("Please enter name of person receiving money: ");
         String receive = scan_interdebit2.nextLine();
         System.out.print("Please enter amount you want to transfer: ");
         double account_deposit = scan_interdebit3.nextDouble();
         Inov2.send_money_debit_international(account_num, account_deposit, receive);
    }

    public static void Currency_exchange() throws SQLException, IOException {
        inov Inov2 = new inov();
        Scanner scan_interdebit = new Scanner(System.in);
        // Scanner scan_interdebit2 = new Scanner(System.in);
        Scanner scan_interdebit3 = new Scanner(System.in);
        Scanner scan_interdebit4 = new Scanner(System.in);
        System.out.print("Please enter virtual account number: ");
        int account_num = scan_interdebit.nextInt();
        System.out.println("Please select ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        // System.out.println("3. International Debit ");
        String accnt_line = scan_interdebit3.nextLine();
        System.out.println("Please select ?");
        System.out.println("1. Euros ");
        System.out.println("2. British Pounds ");
        System.out.println("3. Australian Dollars ");
        System.out.println("4. Japanese Yen ");
        System.out.println("5. Hong Kong Dollars ");
        String curr_convert = scan_interdebit4.nextLine();
        if (accnt_line.equals("1"))
            if (curr_convert.equals("1")){
                Inov2.Currency_exchange_Debit_EUR(account_num);
        } if (accnt_line.equals("1"))
            if (curr_convert.equals("2")){
                Inov2.Currency_exchange_Debit_GBP(account_num);
            }
        if (accnt_line.equals("1"))
            if (curr_convert.equals("3")){
                Inov2.Currency_exchange_Debit_AUS(account_num);
            }
        if (accnt_line.equals("1"))
            if (curr_convert.equals("4")){
                Inov2.Currency_exchange_Debit_JPY(account_num);
            }
        if (accnt_line.equals("1"))
            if (curr_convert.equals("5")){
                Inov2.Currency_exchange_Debit_HKD(account_num);
            }
        if (accnt_line.equals("2"))
            if (curr_convert.equals("1")){
                Inov2.Currency_exchange_Credit_EUR(account_num);
            } if (accnt_line.equals("2"))
            if (curr_convert.equals("2")){
                Inov2.Currency_exchange_Credit_GBP(account_num);
            }
        if (accnt_line.equals("2"))
            if (curr_convert.equals("3")){
                Inov2.Currency_exchange_Credit_AUS(account_num);
            }
        if (accnt_line.equals("2"))
            if (curr_convert.equals("4")){
                Inov2.Currency_exchange_Credit_JPY(account_num);
            }
        if (accnt_line.equals("2"))
            if (curr_convert.equals("5")){
                Inov2.Currency_exchange_Credit_HongKong(account_num);
            }


    }


    public static void main(String[] args) throws NoSuchAlgorithmException, SQLException, IOException {
        intro();
    }
}
