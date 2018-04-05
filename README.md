# off
My experiment with Open Food Facts Data

1. Analysis For Preprocessing pipeline<br>
   https://docs.google.com/spreadsheets/d/1MIY0tk2Wn6ENMRpnJgsSQogDFSt0rL4a3Aw7f1VhZ7I/edit#gid=964778600
2. Autorotate text<br>
   This code first grabs all coordinates with pixel value>0, compute minimum bounded rectangle and get the skew angle.(Also        handles  90 degree rotated text). This works fine provided we give preprocessed images. Will be updating more on this          shortly.
3. Deblur<br>
   Applied weiner filter in scikit learn to deblur images.

   
