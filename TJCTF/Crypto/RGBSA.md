# rgbsa

Extract red pixel vals from each frame (last bit)
go to day's site

 https://medium.com/bugbountywriteup/rsa-attacks-common-modulus-7bdb34f331a5 
 
copy code with adjustments. convert output to text and bam! 
#### flag{excitable_illumination_wanderer_}

```python
def main():
    from PIL import Image, ImageFilter

    def openshit(filename):
        # Open image file
        im = Image.open(filename)

        print("\n** Analysing image **\n")

        # Display image format, size, colour mode
        print("Format:", im.format, "\nWidth:", im.width, "\nHeight:", im.height, "\nMode:", im.mode)

        # Check if GIF is animated
        frames = im.n_frames

        print("Number of frames: " + str(frames))
        print("\n** Converting image **\n")

        alls = []
        # Iterate through frames and pixels, top row first
        for z in range(frames):
            # Go to frame
            im.seek(z)
            rgb_im = im.convert('RGB')
            # print("Frame: ", im.tell())

            pixels = list(rgb_im.getdata())

            a = int("".join([str(r[0]%2) for r in pixels]),2)
            # print("--------------------------------------")
            # print(a)
            # print("--------------------------------------")
            alls.append(a)

        return alls


    alln = openshit("n.gif")
    alle = openshit("e.gif")
    allc = openshit("new_c.gif")
```
