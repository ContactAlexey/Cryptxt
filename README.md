<body>

<h1>Cryptxt</h1>

<p>
    <span>Python 3.x</span>
    <span>MIT License</span>
    <span>Kali Linux</span>
</p>

<p><strong>Cryptxt</strong> is an encryption tool for Kali Linux that allows you to encrypt messages inside text files (<code>.txt</code>) using a system based on ASCII and binary. It is ideal for securely protecting textual information in a simple way.</p>

<h2>Features</h2>
<ul>
    <li>Encrypt messages in <code>.txt</code> files.</li>
    <li>Convert characters to ASCII and binary.</li>
    <li>Multiply by a random number to increase security.</li>
    <li>Generates a <code>hidden_message.txt</code> file with the encrypted message.</li>
    <li>Easy to install and use from the Kali Linux terminal.</li>
</ul>

<h2>Installation</h2>
<p>Clone the repository and install Cryptxt:</p>
<pre><code>git clone https://github.com/ContactAlexey/cryptxt.git
cd cryptxt
chmod +x install.sh
./install.sh</code></pre>

<p>This will install Cryptxt and give it execution permissions.</p>

<h2>Usage</h2>
<p>1. Navigate to the directory where your <code>.txt</code> file is located.</p>
<p>2. Run:</p>
<pre><code>cryptxt &lt;file.txt&gt;</code></pre>
<p>3. A <code>hidden_message.txt</code> file will be generated containing the encrypted content.</p>

<h2>How it works</h2>
<ol>
    <li>The text from the file is read.</li>
    <li>Each character is converted to its ASCII value.</li>
    <li>The ASCII value is converted to binary.</li>
    <li>Each binary value is multiplied by a random number.</li>
    <li>This random number is stored at the end of the file to allow future decryption.</li>
</ol>

<p>The resulting file contains multiplied binary numbers and the encryption number at the end:</p>
<pre><code>123 456 789 ... &lt;random_number&gt;</code></pre>

<h2>Example</h2>
<p>File <code>message.txt</code>:</p>
<pre><code>Hello World</code></pre>

<p>Command:</p>
<pre><code>cryptxt message.txt</code></pre>

<p>Output in <code>hidden_message.txt</code>:</p>
<pre><code>696 1056 1856 2112 528 1584 2112 2112 1056 1104 2112 42</code></pre>

<p><em>Note:</em> 42 is the random number used for multiplication.</p>

<h2>License</h2>
<p>MIT License – free for personal and educational use.</p>

</body>
