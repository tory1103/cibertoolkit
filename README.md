<p align="center">
  <a href="https://github.com/tory1103/cibertoolkit" rel="noopener">
  <img src="docs/images/logo.png" alt="logo"></a>
</p>

<h3 align="center">Automated pentesting framework</h3>

<div align="center">

  ![GitHub status](https://img.shields.io/badge/status-active-brightgreen)
  ![GitHub issues](https://img.shields.io/github/issues/tory1103/cibertoolkit?color=yellow)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/tory1103/cibertoolkit?color=purple)
  ![GitHub license](https://img.shields.io/github/license/tory1103/cibertoolkit?color=blue)
  ![GitHub last commit](https://img.shields.io/github/last-commit/tory1103/cibertoolkit?color=red)
  ![Python version](https://img.shields.io/badge/Python-3.8+-orange?logo=python")
  ![Version](https://img.shields.io/badge/version-Alpha-cyan?logo=python")

</div>

---


**Ciber-Toolkit** is a framework designed to automate the process of downloading and installing different penetration testing tools . It's based in [ToolKit Framework](https://github.com/AdrMXR/KitHack)


## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](./TODO.md)
- [Contributing](./CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)
- [Useful Links](#links)

## 🧐 About <a name = "about"></a>
Ciber-Toolkit is an improved version of [ToolKit Framework](https://github.com/AdrMXR/KitHack). Most important differences are:
  - Tested tools - Download and installation is completed on every OS
  - Modular tools - The download and install script is not needed to be modified, just .json file
  - Docker support - Docker image alternatives

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites
```requirements.txt
oh-my-pickledb==0.4
termcolor==1.1.0
```

### Installing
```bash
# Installing using github
$ git clone https://github.com/tory1103/cibertoolkit
$ cd cibertoolkit
$ sudo bash install.sh -y # For automated installation, remove 'y' parameter if wanted

# Installing using docker
$ docker pull adriantoral/cibertoolkit
$ docker run -it --name toolkit adriantoral/cibertoolkit

# If port forwarding is needed, use this one instead
$ docker run -it --name toolkit -p <host_port>:<docker_port> adriantoral/cibertoolkit

```

## 🎈 Usage <a name="usage"></a>
```bash
# Once installed, if shortcut created, run:
$ sudo toolkit

# Else, run:
$ cd src/ciber-toolkit && sudo python3 toolkit.py

# If you want to build docker image, run:
$ docker build -t cibertoolkit .
$ docker run -it --name toolkit cibertoolkit

# Or download it from docker hub, run:
$ docker pull adriantoral/cibertoolkit
$ docker run -it --name toolkit adriantoral/cibertoolkit
```

## ⛏️ Built Using <a name = "built_using"></a>
- Python
- Json
- Bash (sh)
- Docker

## ✍️ Authors <a name = "authors"></a>
- [@tory1103](https://github.com/tory1103) - Idea, Concept & Initial work

See also the list of [contributors](https://github.com/tory1103/cibertoolkit/contributors) who participated in this project.

<p align="center">
  <a href="https://github.com/tory1103/cibertoolkit/graphs/contributors">
    <img src="https://contributors-img.web.app/image?repo=tory1103/cibertoolkit"  alt=""/>
  </a>
</p>

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- [json](https://www.json.org/json-en.html) 
- [bash](https://es.wikipedia.org/wiki/Bash)
- [docker](https://www.docker.com/)


## ✨ Useful links <a name = "links"></a>
- [Docker Hub](https://hub.docker.com/repository/docker/adriantoral/cibertoolkit)