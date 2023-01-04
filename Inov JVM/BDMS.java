import java.sql.*;

public class BDMS {



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


    //Debit Account systems
    public static void debit_accounts() throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_debit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovDEBIT");
        while (retract_debit.next()) {
            String account_name = retract_debit.getString("NAME");
            int card_num = retract_debit.getInt("CARDNUM");
            String card_code = retract_debit.getString("CARDCODE");
            double checking_balance = retract_debit.getDouble("CHECKING");
            double saving_balance = retract_debit.getDouble("SAVING");
            String address = retract_debit.getString("ADDRESS");
            String currency = retract_debit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
        }
    }

    //delete account
    public String delete_account_debit(int Cardnum) throws SQLException {
        String debit_sql = "DELETE * FROM InovDEBIT WHERE CARDNUM=?";
        Statement state = connect().createStatement();
        // Debit account check
        PreparedStatement stat = connect().prepareStatement(debit_sql);
        stat.setDouble(1, Cardnum);
        return "account deleted";

    }

    public static void credit_accounts() throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_credit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovCREDIT");
        while (retract_credit.next()) {
            String account_name = retract_credit.getString("NAME");
            int card_num = retract_credit.getInt("CARDNUM");
            String card_code = retract_credit.getString("CARDCODE");
            double checking_balance = retract_credit.getDouble("CHECKING");
            double saving_balance = retract_credit.getDouble("SAVING");
            String address = retract_credit.getString("ADDRESS");
            String currency = retract_credit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
            }
        }

    //delete account
    public String delete_account_credit(int Cardnum) throws SQLException {
        String debit_sql = "DELETE * FROM InovCREDIT WHERE CARDNUM=?";
        Statement state = connect().createStatement();
        // Debit account check
        PreparedStatement stat = connect().prepareStatement(debit_sql);
        stat.setDouble(1, Cardnum);
        return "account deleted";
    }

    //International Debit Account systems
    public static void International_debit_accounts() throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_debit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovInterDEBIT");
        while (retract_debit.next()) {
            String account_name = retract_debit.getString("NAME");
            int card_num = retract_debit.getInt("CARDNUM");
            String card_code = retract_debit.getString("CARDCODE");
            double checking_balance = retract_debit.getDouble("CHECKING");
            double saving_balance = retract_debit.getDouble("SAVING");
            String address = retract_debit.getString("ADDRESS");
            String currency = retract_debit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
        }
    }

    //delete account
    public String delete_account_InternationalDebit(int Cardnum) throws SQLException {
        String debit_sql = "DELETE * FROM InovInterDEBIT WHERE CARDNUM=?";
        Statement state = connect().createStatement();
        // Debit account check
        PreparedStatement stat = connect().prepareStatement(debit_sql);
        stat.setDouble(1, Cardnum);
        return "account deleted";
    }

        public static void main(String[] args) throws SQLException, ClassNotFoundException {
            credit_accounts();
            International_debit_accounts();
            debit_accounts();
    }
}


