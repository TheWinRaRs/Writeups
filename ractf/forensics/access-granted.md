# Access Granted

When opening the video file, we're greeted with a music video.

After running strings, we can see 'password{guitarmass}' and when using binwalk we can get an image that simply says 'password{guitarmass}'.

It's clear we need this password for something, but what and where?

My initial assumptions were using steghide on the files or the video's thumbnail - but of course, nothing.

I immediately got to researching MP4 steganography techniques and found many articles that covered hiding TrueCrypt volumes within an MP4.

While TrueCrypt is now outdated and has many security flaws, I tried mounting the MP4 file, using the password I had found - and again, nothing.

However, with more research I had found that a more secure alternative exists: VeraCrypt.

Now, there weren't any articles I could find about hiding VeraCrypt volumes within an MP4 but I was hopeful and still tried.

I installed VeraCrypt and attempted to mount the MP4, alongside using the password.

And there it was:

flag.png

Opening the .png will give us the flag.

## Flag: ractf{Butt3rsn00k's\_R3veng3}

