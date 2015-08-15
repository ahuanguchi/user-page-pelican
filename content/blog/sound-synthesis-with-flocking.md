Title: Sound synthesis with Flocking
Category: JavaScript

As I was revisiting the [bullet hell game](http://d-m-adventure.neocities.org/canvasgame.html) I made as part of my Christmas gift to my friends last year, I realized that it was a bit strange that some of the other pages on my site had music and that I'd even added an entire music section later but the game had no audio at all. To fix this, I searched for JavaScript sound synthesis libraries and came upon [Flocking](http://flockingjs.org). Their front page caught my attention with this: "In Flocking, unit generators and synths are specified declaratively as JSON, making it easy to save, share, and manipulate your synthesis algorithms."

Indeed, I found it much more intuitive to customize sounds in Flocking compared to other audio libraries I've used before. Instead of awkwardly using a chain of object methods to patch different components together before patching to the output, you can make a self-contained JavaScript object that defines a synthesizer with all of the unit generators it depends on:

    :::javascript
    var explodeSynthObj = {
      synthDef: {
        ugen: "flock.ugen.lfNoise",
        freq: 2000,
        mul: {
          ugen: "flock.ugen.asr",
          attack: 0.001,
          sustain: 0.25,
          release: 0.5,
          gate: {
            ugen: "flock.ugen.inputChangeTrigger",
            source: 1,
            duration: 0
          }
        }
      }
    };

Then you can simply pass your object as a parameter to `flock.synth()` to start and return a new instance that you can call `.play()` or `.pause()` on as needed.

Additionally, the official website of Flocking has a [playground](http://flockingjs.org/demos/interactive/html/playground.html#asr) where you can try different presets and interactively modify them, which makes it easy to figure out how different unit generators work.

Currently, the sounds I've added to my game include the above explosion effect, an impulse oscillator that quickly plays random frequencies between 220 Hz (A3) and 440 Hz (A4) while fighting normal enemies, and a pulse wave oscillator that slowly plays random frequencies between 55 Hz (A1) and 77.7817 Hz (D#2) while fighting bosses.
