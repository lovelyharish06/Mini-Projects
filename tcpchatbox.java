import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.*;
import java.io.IOException;
import java.util.Scanner;

public class tcpchatbox{
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Port to listen : ");
        int p1=sc.nextInt();
        System.out.print("Enter Port to Send : ");
        int p2=sc.nextInt();
        InetAddress ip=InetAddress.getLocalHost();
        new Thread(()->{
            try{
                ServerSocket ss=new ServerSocket(p1);
                Socket socket=ss.accept();
                BufferedReader bf=new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String str;
                while(true){
                    str=bf.readLine();
                    if(str==null || str.equals("bye")){break;}
                    System.out.println("::-"+str);
                }
                socket.close();ss.close();
            }catch(IOException e){
                System.out.println("Stopped..");
            }
        }).start();
        new Thread(()->{
            Socket socket=null;
            while(socket==null){
                try {
                    socket = new Socket(ip, p2);
                }catch (IOException e) {
                    try {
                        Thread.sleep(500);
                    }catch(InterruptedException ex){}
                }
            }
            try{
                PrintStream ps=new PrintStream(socket.getOutputStream(),true);
                BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                String msg;
                while(true){
                    msg=br.readLine();
                    ps.println(msg);
                    if(msg==null || msg.equalsIgnoreCase("bye")){break;}
                }socket.close();
            }catch(IOException e){
                System.out.println("Stopped..");
            }
        }).start();
    }
}
