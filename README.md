# AWS CDKTF S3

![cdktf](https://img.shields.io/badge/cdktf-0.11.2-informational)
![Twitter Follow](https://img.shields.io/twitter/follow/abdelFare?logoColor=lime&style=social)

This repository contains a basic code to create an s3 bucket using [Cloud Development Kit and Terraform](https://www.terraform.io/cdktf).

## Usage

1. Install the cdktkf cli `npm i -g cdktf-cli@latest`
2. Clone this Repo `git clone https://github.com/abdelino17/aws-cdktf-samples-s3`
3. Navigate to the new folder `cd aws-cdktf-samples-s3`
4. Create the virtualenv with [pipenv](https://pipenv.pypa.io/en/latest/) and install the required packages `pipenv install`
5. Generate the terraform state of your project with the command `cdktf synth`
6. Deploy your stack `cdktf deploy`
