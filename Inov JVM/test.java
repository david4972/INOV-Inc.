import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import java.io.UnsupportedEncodingException;
public class test {

    public static void main(String[] args) throws UnsupportedEncodingException {
        send_mail_deposit_Saving("davidokoronkwo7@gmail.com", 20.0);
    }

    public static void send_mail_deposit_Saving(String mail, double deposit) {
        Properties props = new Properties();
        Session session = Session.getDefaultInstance(props, null);

        try {
            Message msg = new MimeMessage(session);
            msg.setFrom(new InternetAddress("monetarytransatlantic@gmail.com", "Deposit Inov"));
            msg.addRecipient(Message.RecipientType.TO,
                    new InternetAddress(mail, " User"));
            msg.setSubject("Your Deposit has been made");
            msg.setText("Your deposit of $" + deposit + "has been made to your savings account.");
            Transport.send(msg);
        } catch (AddressException e) {
            System.out.println("Address not found");
        } catch (MessagingException e) {
            System.out.println("message not processed");
        } catch (UnsupportedEncodingException e) {
            System.out.println("couldn't send mail");
        }
    }
}





