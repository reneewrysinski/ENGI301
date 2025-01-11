"""
--------------------------------------------------------------------------
Main Alarm Setting and Playing  
--------------------------------------------------------------------------
License:   
Copyright 2024 Renee Wrysinski


Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

"""
import sys
import os
import time 
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from button import Button
from spi_screen import SPI_Display
from buzzer_music import BuzzerMusic

class Tetris():
    """ Tetris """
    button         = None
    debug          = None
    music          = None
    buzzer         = None
    
    def __init__(self, a_button="P1_36", 
                       b_button="P1_34",
                       r_button="P1_32",
                       d_button="P1_30",
                       l_button="P1_28",
                       u_button="P1_26",
                       buzzer="P2_3",
                       debug=False):
        """ Initialize variables and set up display """

        self.a_button         = Button(a_button)
        self.b_button         = Button(b_button)
        self.r_button         = Button(r_button)
        self.d_button         = Button(d_button)
        self.l_button         = Button(l_button)
        self.u_button         = Button(u_button)
        
        self.display        = SPI_Display()
        
        self.music          = BuzzerMusic(buzzer)
        
        
        
    def run(self):
        self.display.image("tetris.jpg")
        
        self.music.play_song_from_list(13, zero_index=True)
        time.sleep(1.6)
        self.music.play_song_from_list(13, zero_index=True)
        time.sleep(1.6)
        self.music.play_song_from_list(13, zero_index=True)

    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Set Display to show program is complete
        self.display.text("done")

        # Clean up hardware
        self.button.cleanup()
        self.music.cleanup()
        
        
        
# Main script

if __name__ == '__main__':

    print("Program Start")
    
    tetris = Tetris()
    
    try:
        tetris.run()
        
    except KeyboardInterrupt:
        # Clean up hardware when exiting
        tetris.cleanup()