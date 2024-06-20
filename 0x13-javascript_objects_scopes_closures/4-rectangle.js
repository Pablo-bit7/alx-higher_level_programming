#!/usr/bin/node
// Defines a Rectangle class with width and height attributes

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the rectangle using the character 'X'
  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Method to swap the width and height of the rectangle
  rotate() {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  // Method to double the width and height of the rectangle
  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

