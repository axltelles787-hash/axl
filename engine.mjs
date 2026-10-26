export class Motion {
 constructor(length=8){this.length=length;this.position=0;this.speed=0;this.setpoint=.2;this.direction=0;this.emergency=false;this.target=null;this.elapsed=0;this.distance=0;this.limit=null}
 command(dir){if(this.emergency)return false;if((dir<0&&this.position<=0)||(dir>0&&this.position>=this.length))return false;this.direction=dir;this.target=null;this.limit=null;return true}
 stop(){this.direction=0;this.speed=0;this.target=null}
 estop(){this.stop();this.emergency=true}
 reset(){this.emergency=false;this.stop()}
 home(){if(this.command(-1)){this.target=0;return true}return false}
 step(dt){dt=Math.max(0,Math.min(dt,.1));if(!this.direction||this.emergency){this.speed=0;return null}this.elapsed+=dt;this.speed=Math.min(this.setpoint,this.speed+.35*dt);let before=this.position;this.position=Math.max(0,Math.min(this.length,this.position+this.direction*this.speed*dt));this.distance+=Math.abs(this.position-before);if(this.position===0||this.position===this.length){this.limit=this.position===0?'inicio':'final';this.stop();return this.limit}return null}
}
