# BIOE340

## Course: Modeling Physiological Systems

We covered a broad array of topics from cell and general physiology, circulation, metabolism, and the nervous system. In lab, we analyze muscle contractions in a frog leg to understand the refractory period and conducted an ECG analysis on a classmate with Matlab.

### ECG Signals Analysis Lab

**Challenges:** The ECG data captured in lab was noisy and realistic, which made determining the relevant peaks for analysis difficult

Using Matlab, we first had to de-trend the data to establish a clear baseline. We then applied a Savitzky-Golay transform to smooth out the graph and eliminate oscillation and noise around the peaks. With a cleaner signal, we could collect an array of all of the local maxima and minima. Filtering out any points not following the P-QRS-T pattern, the final dataset is ready for diagnosis. After calibrating the algorithm to a sample data set, we could now dynamically analyze new data sets in close to real time.

Combined ECG leads with highlighted peaks:

![TBD](./imgs/bioe340/mathematica_01.png)

For the last step of diagnosis, we needed to capture the mean electrical axis of the heart. The axis pointing down and to the right suggests normal heart depolarization and a diagnosis of no Bradycardia.

Mean Electrical Axis:

![TBD](./imgs/bioe340/mathematica_02.png)
