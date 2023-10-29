# Spotify-Api-Automated-Extraction-Transformation-S3
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/76b2e7ca-7db8-4360-8adf-609c662a8da0)

Steps

1) Create Spotify Account on https://developer.spotify.com/

2) Create App
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/dd8e788f-22b3-4745-8c78-fd2af9003103)

3) Collect Client ID and Secret Details
![Screenshot 2023-10-29 at 3 26 14 PM](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/7bbbaf89-0f1e-47fb-aa02-a0d8974d52f7)

4) Validate the Connection through below Code
https://colab.research.google.com/drive/1y-Ih-huGMwAMv91564INRKtcFyTrWeP6#scrollTo=Fnm1MitZCLJO

5) Do required Transformations to Extract Required List of Data (Album, Artist, Songs List)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/b70d4861-e668-46e3-9214-f2a78a6130bc)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/4b0b9552-ab0e-455f-b54a-49926b0e985b)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/7aab8682-c5fb-48c8-9f15-145e216cbda5)

6) On AWS, Create S3 Buckets, Raw (To Process & Processed) & Transformed (with Respective output Album, Artist, Songs folders)

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/c9840bb8-b705-4f16-9b9f-746632d1a541)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/ec1410b9-3f05-40bc-9f0b-691cd788dc24)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/34e32375-2ab9-455b-bfe8-0b692fd8dd8f)

8) On AWS, Create Lambda Functions for Above Extraction Code

9) Create Env Variables

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/acebe6d8-7391-4c0b-b036-9f2e8c0e67ba)

10) Add Extraction Function to Dump Output to S3 Bucket

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/430ad199-8760-4f46-9ce0-efffcefffefe)

11) Add layer to Lambda Function to refer external spotify libraries not supported by lambda (zip file in repo)

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/0aea212a-501b-49db-87d9-6d9fc6b8ec13)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/f5032aa6-7880-4c47-8210-2cad06485e80)

12) Add permissions for Lambda to Communicate with S3 using Role Permission settings

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/eff4d280-4f78-417f-81dc-38453a298796)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/916aaafa-9b00-4dde-9b96-0d9fb6c2d98d)

13) Add Trigger to Invoke Lambda Function using Event Bridge (with frequent interval)

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/89e41e4b-245f-4de5-abef-6a09638b092f)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/c1bde7a0-7fab-4e69-a1a3-ac23a10f85d2)

14) Validate Trigger & Lambda Working by Files Created at S3 Bucket - for every interval - 1 Min/1 Day

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/4d847163-406d-441f-9d02-86d9635e5e78)

15) Create Similar Lambda Func with Permissions (Read Raw from S3 - Lambda Role - Write Transf to S3), Layer(Pandas), Env Variables to read from S3 (Raw Folder) with Trigger from S3 (.json) Present

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/10c2c745-46b2-4b07-a3e2-6c1de4cd5bbf)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/cf5deccd-5b51-4526-b615-ae060c281aaf)
![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/a3b7ee9b-f211-4e23-b04e-185fe489a38c)

16) Validate Transformed File Created under S3

![image](https://github.com/harishavenue1/Spotify-Api-Automated-Extraction-Transformation-S3/assets/21108205/3724a34e-7cb8-434d-90a6-af41fd6ae9d2)




