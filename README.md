# SerDeOps_demo
# **Serialization and Deserialization in Network Programming**  
**A Python example demonstrating JSON serialization between a client and server.**  

## **📌 Overview**  
This project illustrates how **serialization** (converting objects to a transmittable format) and **deserialization** (reconstructing objects from transmitted data) work in a client-server architecture using Python's `socket` and `json` modules.  

### **Key Concepts**  
**Serialization**: Convert Python objects → JSON string (for transmission).  
**Deserialization**: Convert JSON string → Python objects (after receiving).  
**Socket Communication**: Basic TCP connection between client and server.  

---
## **🚀 How to Run**  

### **Prerequisites**  
- Python 3.11+  



### **Steps**  
1. **Clone the repository**:  
   ```sh
   git clone https://github.com/lilkuuks/SerDeOps_demo.git
   cd SerDeOps_demo
   ```

2. **Run the server** (in one terminal):  
   ```sh
   python server.py
   ```
   - The server will start listening on `0.0.0.0:9999`.  

3. **Run the client** (in another terminal):  
   ```sh
   python client.py
   ```
   - The client sends a JSON-serialized dictionary to the server and prints the response.  

---


## **📜 License**  
This project is licensed under **MIT License**.  
