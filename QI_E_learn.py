'''
Introducing Quantun Error Correction by  A. C. Quillem -- 2025.03.17

https://astro.pas.rochester.edu/~aquillen/phy265/lectures/QI_E.pdf
'''

'''
1 Error correction on a quantum computer
    The process of quantum computing(Dream)
    
        1st Initial  Encoding by gates
            Describe with lots of 0 and 1 
        2ed Process
            The qubits are in entangled states(a|0> + b|1>) to efficiently process
        3rd Measurement Decoding
            Decohere qubits to get the outcome 

    Why? 
        Qubit is fragile in all 3 stage because the env disturb(env noise)

            1st maintain the qubit state in what you want
            2ed maintain the a and b
            3rd maintain the output qubit state 

            But in the fact what we really need to care is the 2ed stage

        So we need QEC after Encoding and before Decoding
        And the QEC itself CAN'T disturb the qubit itself(If QEC diturb it, QEC are the biggest problem)
        And another basic thing is that we have know that the quantum gate won't decohere the qubit, so we just 
            need to find a way to use the quantum gate to get the information.

        So right now the QEC is a concept which is defined as a operation matain the a and b.

        And before we go on, we need a fact that the little qubit(a, b) error won't impact the whole process, 
            so we just need to make sure that the QEC can let the error rate of qubits under the 
            threshold all of the time.

        For this reason,we get the basic process of QEC in computing 2ed stage

            run the computing until threshold ──→  stop  ──→  QEC
                      ↑________________________________________↓
            
         

    How QEC?

        1st Figure out which qubit is disturb()
        One state with more qubit. -- repetition code
        1 > 111
        1 physical qubit > 3 physical qubit > 1 logic bit    

        specially 
            1st physical qubit is called data qubit / message qubit
            others are caleed ancilla qubits / syndrome qubits    
'''


'''
2 Three bit Quantum error correction codes

2.1 Correcting bit flip errors with a three bit code

    Basic thing
        1
    0 = 0    
      
                             1
                             0
                             0                      
    00 = 0 tensorproduct 0 = 0

        0 1
    X = 1 0

        1 0
    I = 0 1

    What is a error look like -- bit flip error
        000 > 100    
        000 > 010
        000 > 001

         1     0
         0     0
         0     0
         0     0
         0     1
         0     0
         0     0
         0  >  0

         (X tp I tp I) * 000 = 100
         (X * 0) tp (I * 0) tp (I * 0) = 1 tp 0 tp 0 = 100  

        
'''
