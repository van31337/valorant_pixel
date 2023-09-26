#include <Ethernet.h> // Include the Ethernet library

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED}; // MAC address of the Ethernet shield
IPAddress ip(192, 168, 0, 123); // IP address of the Arduino
EthernetServer server(80); // Create an Ethernet server object on port 80

void setup() {
  Ethernet.begin(mac, ip); // Initialize Ethernet with the provided MAC and IP addresses
  server.begin(); // Start the server
}

void loop() {
  EthernetClient client = server.available(); // Check for incoming client connections

  if (client) { // If a client is connected
    if (client.connected()) {
      // Handle client requests here
      client.println("HTTP/1.1 200 OK"); // Send a response header
      client.println("Content-Type: text/html");
      client.println(); // Empty line to separate header from content
      client.println("<html><body><h1>Hello, world!</h1></body></html>"); // Send the response content
      client.stop(); // Close the connection
    }
  }
}
