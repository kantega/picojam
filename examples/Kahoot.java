import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.util.List;

// Java part of multicast example
public class Kahoot {

    public static void receiveUDPMessage(String ipAddress, int port) {
        byte[] buffer = new byte[1024];
        try (var socket = new MulticastSocket(port)) {
            socket.joinGroup(InetAddress.getByName(ipAddress));
            while (true) {
                System.out.println("Waiting for multicast message...");
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);
                String msg = new String(packet.getData(), packet.getOffset(), packet.getLength());
                System.out.println("Message: " + msg);
            }
        } catch (IOException ioex) {
            System.err.println("Exception while receiving: " + ioex);
        }
    }

    public static void sendUDPMessage(String message, String ipAddress, int port) throws IOException {
        DatagramSocket socket = new DatagramSocket();
        InetAddress group = InetAddress.getByName(ipAddress);
        byte[] msg = message.getBytes();
        DatagramPacket packet = new DatagramPacket(msg, msg.length, group, port);
        socket.send(packet);
        System.out.println("Sent " + message + " to " + ipAddress + ":" + port);
        socket.close();
    }

    private record Q(String q, String a, String b, String c, String d) {
    }

    private static List<Q> qs = List.of(
            new Q("Beste prog", "Java", "Py", "C++", "C#"),
            new Q("Beste arbeidsgiver", "Kantega", "Bekk", "Tieto", "DNB")
    );

    public static void main(String[] args) throws IOException, InterruptedException {
        var UDP_IP = "239.255.255.255";
        var UDP_PORT = 1900;
        new Thread(() -> receiveUDPMessage("239.255.255.255", UDP_PORT)).start();
        for (var q : qs) {
            var json = "{\"to\": \"kahoot-players\", \"q\":\"" + q.q() + "\", \"a\":\"" + q.a() + "\", \"b\":\"" + q.b() + "\", \"c\":\"" + q.c()
                    + "\", \"d\":\"" + q.d() + "\"}";
            sendUDPMessage(json, UDP_IP, UDP_PORT);
            Thread.sleep(10000);
        }
    }
}
