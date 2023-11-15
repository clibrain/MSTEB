FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel
COPY requirements.txt ./
WORKDIR ./ 
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
ENTRYPOINT [ "python" ]

