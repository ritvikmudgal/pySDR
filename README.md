<h1 align="center"> <b><i><u> pySDR</u></i></b></h1>
<h2>1. Introduction</h2>
<p><b><i>SDR</i></b>- SDR stands for software Defined Radio, which is nothing but an alternative to those old hardwares connected to radios to transmit and receive signals<br> It is very flexible compared to those hardwares, to modulate/demodulate frequencies you just have to change the code and boom! <br>
<b><i>DSP</i></b>- It stands for Digital Signal Processing, whenever we receive a signal using SDR, we convert it into complex numbers and perform math/programming on that to extract information is called DSP
<h2>2. Frequency domain</h2>
<p><b><i>Fourier Series</i></b>- Any signal is made up by summing up multiple sine waves, so its constituent sine waves are called fourier series<br>
<b><i>Fourier Transform</i></b>- The conversion of a frequency phase to time phase or reverse is called Fourier Transform<br>
<b><i>FFT</i></b>- It stands for Fast Fourier Transform, It is just an algorithm to perform Fourier Transform <br>
 ex. We have a sine wave:<br>
 (sin-wave.png)

<br> To use FFT we just have to add one line, <br><i>
S = np.fft.fft(s)</i><br>
<b><i>Windowing</i></b>- FFT assumes that a slice of signal continues infinitely so it connects the end and starting, but due to having differenct characterstics and both end and start it does't blend nicely and so to correct that, we just multiply starting and ending with zero phase(Hamming) which makes them connect super neatly and reduces error.<br>
To perform windowing we just have to add a line of code to our previous codes: <br><i>
s = s * np.hamming(100)</i>
