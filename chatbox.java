import java.io.IOException;
import java.util.Scanner;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
public class chatbox {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Port to listen : ");
        int p1=sc.nextInt();
        System.out.print("Enter Port to Send : ");
        int p2=sc.nextInt();
        DatagramSocket ds = new DatagramSocket(p1);
        InetAddress ip = InetAddress.getLocalHost();
        Thread receive=new Thread(()->{
            try{
                byte[] buf = new byte[1024];
                while (true) {
                    DatagramPacket dp = new DatagramPacket(buf, buf.length);
                    ds.receive(dp);
                    String s = new String(dp.getData(), 0, dp.getLength());
                    System.out.println("::-"+s);
                    if (s.equalsIgnoreCase("bye")) {break;}
                }
            }catch(Exception ex){
                System.out.println("Stopped..");
            }
        });
        receive.start();
        Thread send=new Thread(()->{
            try {
                while (true) {
                    String msg = sc.nextLine();
                    DatagramPacket dp = new DatagramPacket(msg.getBytes(), msg.length(), ip, p2);
                    ds.send(dp);
                    if (msg.equalsIgnoreCase("bye")) {break;}
                }
            }catch(Exception ex){
                System.out.println("Stopped..");
            }
            });
        send.start();
    }
}
