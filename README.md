Varia ML is a local GPT for that old PC.<br>
It does not require an API key or internet to work. <br>
This is an ongoing passion project.<br>
A way to interact with an LLM on your machine.<br>
<br>
Varia was intentially built in a 6 year old Windows laptop with only 8GB of RAM. <br>
If your machine has more than that, then you should be able to run this even faster. <br>

<br>
It uses: <br>
- ollama. <br>
- Llama index. <br>
- Model: TinyLlama. <br>
- Coded in Python. <br>
- IDE: PyCharm. <br>

<br>
For more detailed steps, I've documented the whole process thus far on my site: <br>
https://AshNoor.me/

<br><br>
---------------------- <br>
Quick Notes for set up on Windows. <br>
---------------------- <br>
<br>
- Download and Install Ollama (  https://ollama.com/  ). <br>
- (optional) create a python virtual environment. <br>
- Activate said environment. <br>

<br> <br>
- Install the following Python Libraries: <br>
pip install ollama, llama-index-llms-ollama

<br> <br>
- Use ollama to pull the "tinyLlama" model. <br>
ollama pull tinyllama <br>

<br>
* IMPORTANT: *<br>
Make sure to RUN the Ollama.exe on your local machine. <br>
You should see the Ollama icon show up in your service tray. 

<br><br>
Now, you should be able to import and run Varia on your system via the IDE of your choice. <br>
Once you see the prompt, you can then turn off your WiFi if you like. <br>
Enjoy.
