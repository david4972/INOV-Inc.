import java.sql.*;

public class invp {

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

    // Debit
    public void getCard_Debit(String CardCode, double price) throws SQLException {
        //String debit_sql = "SELECT * FROM DEBIT WHERE CARD-CODE=?";
        //String credit_sql = "SELECT * FROM CREDIT WHERE CARD-CODE=?";
        Statement state = connect().createStatement();
        // find account for requested bank statement (credit check)
        ResultSet retract_debit = state.executeQuery("SELECT * FROM InovDEBIT WHERE CARDCODE=?");
        String email = retract_debit.getString("EMAIL");
        String name = retract_debit.getString("NAME");
        retract_debit.close();
        state.close();
        chargeCard_Debit(name, CardCode, price);
    }


    public void chargeCard_Debit(String name, String CardCode, double price) throws SQLException {
        String Vendor = "INVP";

        Statement state = connect().createStatement();;
        // find account for requested bank statement (debit check)
        ResultSet retract_debit = state.executeQuery("SELECT * FROM InovDEBIT WHERE CARDCODE=?, WHERE NAME=?");
        String charge = "UPDATE InovDEBIT set CHECKING=CHECKING-? WHERE CARDCODE=?";
        PreparedStatement stat = connect().prepareStatement(charge);
        stat.setDouble(1, price);
        stat.setString(2, CardCode);
        retract_debit.close();
        String Payment_info = "Account name = " + name + "\n" +
                "Vendor = " + Vendor + "\n" +
                "Amount = " + price + "\n";
        process_payment_Debit(Payment_info);
    }

    public void process_payment_Debit(String message){
        System.out.print(message);
    }


    // Credit
    public void getCard_Credit(String CardCode, double price) throws SQLException {
        //String debit_sql = "SELECT * FROM DEBIT WHERE CARD-CODE=?";
        //String credit_sql = "SELECT * FROM CREDIT WHERE CARD-CODE=?";
        Statement state = connect().createStatement();
        // find account for requested bank statement (credit check)
        ResultSet retract_debit = state.executeQuery("SELECT * FROM InovCREDIT WHERE CARDCODE=?");
        String email = retract_debit.getString("EMAIL");
        String name = retract_debit.getString("NAME");
        retract_debit.close();
        state.close();
        chargeCard_Credit(name, CardCode, price);
    }


    public void chargeCard_Credit(String name, String CardCode, double price) throws SQLException {
        String Vendor = "INVP";

        Statement state = connect().createStatement();;
        // find account for requested bank statement (debit check)
        ResultSet retract_debit = state.executeQuery("SELECT * FROM InovCREDIT WHERE CARDCODE=?, WHERE NAME=?");
        String charge = "UPDATE InovCREDIT set CHECKING=CHECKING-? WHERE CARDCODE=?";
        PreparedStatement stat = connect().prepareStatement(charge);
        stat.setDouble(1, price);
        stat.setString(2, CardCode);
        retract_debit.close();
        String Payment_info = "Account name = " + name + "\n" +
                "Vendor = " + Vendor + "\n" +
                "Amount = " + price + "\n";
        process_payment_Credit(Payment_info);
    }

    public void process_payment_Credit(String message){
        System.out.print(message);
    }
}

