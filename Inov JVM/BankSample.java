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
        System.out.println("4. Send Money International Debit");
        System.out.println("5. Currency Exchange");
        System.out.println("6. Delete Account");
        System.out.println("7. Exit");
        String read = scan.nextLine();
        if (read.equals("1")){
            create_accnt();
        } if (read.equals("2")){
            deposit();
        } if (read.equals("3")){
            send_money();
        } if (read.equals("4")){
            international_debit_send_money();
        } if (read.equals("5")){
            Currency_exchange();
        } if (read.equals("6")){
            delete_accnt();
        }
        if (read.equals("7")){
            System.exit(0);
        }
    }

    public static void create_accnt() throws NoSuchAlgorithmException, SQLException, IOException {
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


    public static void deposit() throws SQLException, NoSuchAlgorithmException, IOException {
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

    public static void create_accnt_debit() throws NoSuchAlgorithmException, SQLException, IOException {
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
        System.out.println("Enter Amount you want to Deposit into Checking account (minimum deposit $25 ):  ");
        double checking = scan.nextDouble();
        System.out.println("Enter Amount you want to Deposit into Saving account (minimum deposit $25):  ");
        double saving = scan.nextDouble();
        Inov.create_debit_account(account_name, account_email, account_address, checking, saving);
        intro();
    }

    public static void create_International_accnt_debit() throws NoSuchAlgorithmException, SQLException, IOException {
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
        System.out.println("Enter Amount you want to Deposit into Checking account (minimum deposit $25 ):  ");
        double checking = scan.nextDouble();
        System.out.println("Enter Amount you want to Deposit into Saving account (minimum deposit $25):  ");
        double saving = scan.nextDouble();
        Inov.create_International_debit_account(account_name, account_email, account_address, account_country, checking, saving);
        intro();
    }

    public static void create_accnt_credit() throws NoSuchAlgorithmException, SQLException, IOException {
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
        System.out.println("Enter Amount you want to Deposit into Checking account (minimum deposit $25 ):  ");
        double checking = scan.nextDouble();
        System.out.println("Enter Amount you want to Deposit into Saving account (minimum deposit $25):  ");
        double saving = scan.nextDouble();
        Inov.create_credit_account(account_name, account_email, account_address, checking, saving);
        intro();
    }

    public static void send_money() throws SQLException, IOException, NoSuchAlgorithmException {
        Scanner scan4 = new Scanner(System.in);
        System.out.print("Will you be sending money with Internationally today?: ");
        System.out.print("1. Yes ");
        System.out.print("2. No ");
        String inter_choice = scan4.nextLine();
        if (inter_choice.equals("1")) {
            send_money_International();
        } if (inter_choice.equals("2")){
            send_money_credit_debit();
        }

    }

    public static void send_money_credit_debit() throws SQLException {
        inov Inov = new inov();
        Scanner scan = new Scanner(System.in);
        Scanner scan2 = new Scanner(System.in);
        Scanner scan3 = new Scanner(System.in);
        Scanner scan4 = new Scanner(System.in);
        System.out.print("Please enter virtual account number: ");
        int account_num = scan.nextInt();
        System.out.print("Please enter name of person receiving money: ");
        String receive = scan2.nextLine();
        System.out.print("Please enter amount you want to send: ");
        double account_deposit = scan.nextDouble();
        System.out.println("Please select your account ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        String accnt_line = scan3.nextLine();
        System.out.println("Please select account you'll be sending to ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        String accnt_line2 = scan4.nextLine();
        // Debit
        if (accnt_line.equals("1") && accnt_line2.equals("1")){
            Inov.send_money_debit(account_num, account_deposit, receive);
        }if (accnt_line.equals("1") && accnt_line2.equals("2")){
            Inov.send_debit_to_credit(account_num, account_deposit, receive);
        }
        //Credit
        if (accnt_line.equals("2")&& accnt_line2.equals("2")){
            Inov.send_money_credit(account_num, account_deposit, receive);
        } if (accnt_line.equals("2")&& accnt_line2.equals("1")){
            Inov.send_credit_to_debit(account_num, account_deposit, receive);
        }
    }

    public static void send_money_International() throws SQLException, IOException, NoSuchAlgorithmException {
        inov Inov2 = new inov();
        Scanner scan_interdebit = new Scanner(System.in);
        Scanner scan_interdebit2 = new Scanner(System.in);
        Scanner scan_interdebit3 = new Scanner(System.in);
        Scanner scan_interdebit4 = new Scanner(System.in);
        Scanner scan_interdebit5 = new Scanner(System.in);
        Scanner scan_interdebit6 = new Scanner(System.in);
        System.out.print("Are you sending money to an international account today?");
        System.out.print("1. Yes");
        System.out.print("2. No");
        String account_choice = scan_interdebit6.nextLine();
        if (account_choice.equals("1")){
            System.out.print("Please enter virtual account number: ");
            int account_num = scan_interdebit.nextInt();
            System.out.print("Please enter name of person receiving money: ");
            String receive = scan_interdebit2.nextLine();
            System.out.print("Please enter amount you want to transfer: ");
            double account_val = scan_interdebit3.nextDouble();
            System.out.print("Please enter Country code of Country you are located Ex USD (United States): ");
            String account_base_currency = scan_interdebit4.nextLine();
            System.out.print("Please enter name of Country where person receiving money is located: ");
            String account_convert_currency = scan_interdebit5.nextLine();
            Inov2.credit_debit_to_international(account_base_currency, account_convert_currency, account_num, account_val, receive);
            intro();
        } if (account_choice.equals("2")){
            international_debit_send_money();
        }


    }

    public static void international_debit_send_money() throws SQLException, IOException, NoSuchAlgorithmException {
         inov Inov2 = new inov();
         Scanner scan_interdebit = new Scanner(System.in);
         Scanner scan_interdebit2 = new Scanner(System.in);
         Scanner scan_interdebit3 = new Scanner(System.in);
         Scanner scan_interdebit4 = new Scanner(System.in);
         Scanner scan_interdebit5 = new Scanner(System.in);
         System.out.print("Please enter virtual account number: ");
         int account_num = scan_interdebit.nextInt();
         System.out.print("Please enter name of person receiving money: ");
         String receive = scan_interdebit2.nextLine();
         System.out.print("Please enter amount you want to transfer: ");
         double account_val = scan_interdebit3.nextDouble();
         System.out.print("Please enter Country code of Country you are located Ex USD (United States): ");
         String account_base_currency = scan_interdebit4.nextLine();
         System.out.print("Please enter name of Country where person receiving money is located: ");
         String account_convert_currency = scan_interdebit5.nextLine();
         Inov2.International_debit_send(account_base_currency, account_convert_currency, account_num, account_val, receive);
         intro();
    }

    public static void Currency_exchange() throws SQLException, IOException, NoSuchAlgorithmException {
        inov Inov2 = new inov();
        Scanner scan_interdebit = new Scanner(System.in);
        Scanner scan_interdebit2 = new Scanner(System.in);
        Scanner scan_interdebit3 = new Scanner(System.in);
        //Scanner scan_interdebit4 = new Scanner(System.in);
        System.out.print("Please enter virtual account number: ");
        int account_num = scan_interdebit.nextInt();
        System.out.print("Please enter Country code of Country you are located Ex USD (United States): ");
        String account_Currency_base = scan_interdebit2.nextLine();
        System.out.print("Please enter name of Country you which to convert currency: ");
        String account_convert_currency = scan_interdebit3.nextLine();
        Inov2.Currency_exchange(account_Currency_base, account_convert_currency, account_num);
        intro();
    }

    public static void delete_accnt() throws SQLException {
        inov Inov2 = new inov();
        Scanner scan_interdebit = new Scanner(System.in);
        Scanner scan_interdebit2 = new Scanner(System.in);
        System.out.print("Please enter virtual account number: ");
        int account_num = scan_interdebit.nextInt();
        System.out.println("Please select account");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        System.out.println("3. International Debit account");
        String read = scan_interdebit2.nextLine();
        if (read.equals("1")) {
            Inov2.delete_debit_account(account_num);
        } if (read.equals("2")) {
            Inov2.delete_credit_account(account_num);
        } if (read.equals("3")) {
            Inov2.delete_International_debit_account(account_num);
        }
    }



    public static void main(String[] args) throws NoSuchAlgorithmException, SQLException, IOException {
        intro();
    }
}
