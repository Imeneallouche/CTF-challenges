FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo


RUN useradd -m -d /home/lm3ne -s /bin/bash lm3ne
RUN echo 'lm3ne:miniCTFHideAndRide' | chpasswd

#COPY THE flag.txt FILE FROM LOCAL TO THE CONTAINER
COPY challenge/.flag.txt /home/lm3ne/.flag.txt
COPY challenge/fake_flag.txt /home/lm3ne/fake_flag.txt

#WORKING DIRECTORY
WORKDIR /home/lm3ne
#MAKE A LINK TO 
RUN ln -s /dev/null .bash_history

#PERMS OF READING THE FILE
RUN chmod 444 /home/lm3ne/flag.txt
RUN chown lm3ne /home/lm3ne/flag.txt



#LISTENING TO PORT 22
EXPOSE 22
#ALWAYS RUN ssh AND DISCARD STDOUT STDERR FROM AN OUTPUT
ENTRYPOINT service ssh start && tail -f /dev/null