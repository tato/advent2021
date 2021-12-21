//! quick visualization
//! 
//! ```cargo
//! [package]
//! edition = "2021"
//! [dependencies]
//! pixels = "0.8.0"
//! winit = "0.25"
//! winit_input_helper = "0.10"
//! ```

use std::collections::HashSet;
use pixels::{Pixels, SurfaceTexture};
use winit::dpi::LogicalSize;
use winit::event::{Event, VirtualKeyCode};
use winit::event_loop::{ControlFlow, EventLoop};
use winit::window::WindowBuilder;
use winit_input_helper::WinitInputHelper;

// must be a clean multiple of problem size
const WINDOW_WIDTH: u32 = 1000;
const WINDOW_HEIGHT: u32 = 1000;

struct Map {
    map: Vec<i32>,
    inner_width: i32,
    inner_height: i32,
    width: i32,
    height: i32,
    processed_risk: Vec<i32>,
    to_process: HashSet<(i32, i32, i32)>,
    processed: HashSet<(i32, i32)>,
}
impl Map {

    fn new() -> Map {

        let data = std::fs::read_to_string("15.txt").unwrap();
        let data = data.split('\n').map(str::trim).collect::<Vec<_>>();
        let width = data[0].len() as i32;
        let height = data.len() as i32;
        let risk_map = data
            .iter()
            .flat_map(|line| line.chars().map(|c| c.to_digit(10).unwrap() as i32))
            .collect::<Vec<_>>();


        let processed_risk = vec![i32::MAX; (width*height*25) as usize];
        let mut to_process = HashSet::new();
        to_process.insert((0, 0, 0));
        let processed = HashSet::new();

        Map { 
            map: risk_map, 
            inner_width: width, 
            inner_height: height, 
            width: width, 
            height: height,
            processed_risk,
            to_process,
            processed,
        }
    }


    fn get(&self, x: i32, y: i32) -> i32 {
        let xi = x / self.inner_width;
        let yi = y / self.inner_height;
        let truex = x % self.inner_width;
        let truey = y % self.inner_height;
        (self.map[(truey*self.inner_width+truex) as usize]+xi+yi-1)%9+1
    }

    
    fn get_min_risk_step(&mut self, frame: &mut [u8]) {
        if !self.to_process.is_empty() {
            let &(posx, posy, risk) = self.to_process.iter().min_by_key(|p| p.2).unwrap();
            self.to_process.remove(&(posx, posy, risk));
            self.processed.insert((posx, posy));
            if posx == self.width-1 && posy == self.height-1 {
                println!("{}", risk);
                return;
            }
            for mov in [(-1,0), (1,0), (0,-1), (0,1)] {
                let nextx = posx+mov.0;
                let nexty = posy+mov.1;
                if nextx < 0 || nexty < 0 || nextx >= self.width || nexty >= self.height {
                    continue;
                }
                if self.processed.contains(&(nextx, nexty)) {
                    continue;
                }
                let nextrisk = risk + self.get(nextx, nexty);
                let prevrisk = self.processed_risk[(nexty*self.width+nextx) as usize];
                if nextrisk < prevrisk {
                    self.processed_risk[(nexty*self.width+nextx) as usize] = nextrisk;
                    self.to_process.insert((nextx, nexty, nextrisk));
                    self.to_process.remove(&(nextx, nexty, prevrisk));
                }
            }
        }
        
        let mut max_risk = 0;
        for y in 0..self.height {
            for x in 0..self.width {
                let risk = self.processed_risk[(y*self.width+x) as usize];
                if risk != i32::MAX && risk > max_risk {
                    max_risk = risk;
                }
            }
        }
        for (i, pixel) in frame.chunks_exact_mut(4).enumerate() {
            let x = (i % WINDOW_WIDTH as usize) as i32;
            let y = (i / WINDOW_WIDTH as usize) as i32;

            let sx: i32 = WINDOW_WIDTH as i32 / self.width;
            let sy: i32 = WINDOW_HEIGHT as i32 / self.height;

            let t = self.processed_risk[(y/sy*self.width+x/sx) as usize] as f32 / max_risk as f32;
            let t = (t * 255.0) as u8;
            pixel.copy_from_slice(&[t, t, t, t])  
        }
    
    }
}





fn main() {
    
    let event_loop = EventLoop::new();
    let mut input = WinitInputHelper::new();
    let window = {
        let size = LogicalSize::new(WINDOW_WIDTH as f64, WINDOW_HEIGHT as f64);
        WindowBuilder::new()
            .with_title("Hello Pixels")
            .with_inner_size(size)
            .with_min_inner_size(size)
            .build(&event_loop)
            .unwrap()
    };

    let mut pixels = {
        let window_size = window.inner_size();
        let surface_texture = SurfaceTexture::new(window_size.width, window_size.height, &window);
        Pixels::new(WINDOW_WIDTH, WINDOW_HEIGHT, surface_texture).unwrap()
    };

    let mut risk_map = Map::new();

    event_loop.run(move |event, _, control_flow| {
        // Draw the current frame
        if let Event::RedrawRequested(_) = event {
            
            risk_map.get_min_risk_step(pixels.get_frame());
            
            if pixels
                .render()
                .is_err()
            {
                *control_flow = ControlFlow::Exit;
                return;
            }
        }

        // Handle input events
        if input.update(&event) {
            // Close events
            if input.key_pressed(VirtualKeyCode::Escape) || input.quit() {
                *control_flow = ControlFlow::Exit;
                return;
            }

            // Resize the window
            if let Some(size) = input.window_resized() {
                pixels.resize_surface(size.width, size.height);
            }

            // Update internal state and request a redraw
            // world.update();
            window.request_redraw();
        }
    });
}