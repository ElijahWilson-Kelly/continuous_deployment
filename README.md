<h1 style="font-weight: 200; font-size: 3rem; border-bottom: 2px solid black">Report</h1>

## Components

---

#### Github Action

Github Actions allows one to automate certain procedures when trigger events are performed (such as pushing to your github repository).
Theses procedures or jobs are defined within the `/.github/workflows` directory in an `.yml` file.
In my case I have defined 2 seperate jobs. The first is reponsible for running the tests to make sure the app is still running as desired and the second is for deploying the app to my DigitalOcean Droplet.

#### Digital Ocean

Digital Ocean is a cloud hosting company that provides virtual servers and storage. By deploying the app on a Droplet (linux-based virtual server) the app will always be live and running on Digital Ocean's hardware.

#### SSH

SSH or Secure Shell Protocol is a way for computers and servers to comunicate with each other without the need for a password. The SSH key is used to login to the (Digital Ocean) virtual server within a Github Action workflow and excute the commands needed to update the app on the server.

## Problems

---

#### Logging in

It was difficult to login to the server within a workflow because the server would always need a password. My way around this problem was to configure both my server and Github repository to allow for SSH communication.

#### Keeping sensitive information secret

The workflow needs access to sensitive information (such as private SSH key) which could potentially be viewed by anyone with access to the repository. To deal with this issue I used Github Secrets. This allowed me to access the information within the workflow by referencing the secret but the information could not be read by anyone else.

#### Pulling from repository

I wasn't able to make a pull request to the repository without some form of authentication so to solve this I used "Deploy Keys". I thought this was the best solution as it limited the scope of the access to only the files that I wanted to pull.
