use rocket::fs::{relative, FileServer};

#[macro_use]
extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", FileServer::from(relative!("/../frontend/build")))
}
