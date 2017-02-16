from database import *
import datetime
engine = create_engine('sqlite:///swimtimes.db')
Base.metadata.bind = engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


session.query(User).delete()
session.query(Swimtime).delete()

user = User(name="Faris",gender="male",age=16,region="Jerusalem")
session.add(user)
session.commit()

swimtimes = Swimtime(stroke="freestyle",time=datetime.time(second=25),distance="50",user=user)
swimtimes1 = Swimtime(stroke="freestyle",time=datetime.time(second=26),distance="50",user=user)
swimtimes2 = Swimtime(stroke="freestyle",time=datetime.time(second=54),distance="100",user=user)
swimtimes3 = Swimtime(stroke="freestyle",time=datetime.time(second=56),distance="100",user=user)
swimtimes4 = Swimtime(stroke="freestyle",time=datetime.time(minute=2,second=15),distance="200",user=user)
swimtimes5 = Swimtime(stroke="freestyle",time=datetime.time(minute=2,second=4),distance="200",user=user)

swimtimes6 = Swimtime(stroke="butterfly",time=datetime.time(second=25),distance="50",user=user)
swimtimes7 = Swimtime(stroke="butterfly",time=datetime.time(second=26),distance="50",user=user)
swimtimes8 = Swimtime(stroke="butterfly",time=datetime.time(second=54),distance="100",user=user)
swimtimes9 = Swimtime(stroke="butterfly",time=datetime.time(second=56),distance="100",user=user)
swimtimes10 = Swimtime(stroke="butterfly",time=datetime.time(minute=2,second=15),distance="200",user=user)
swimtimes11= Swimtime(stroke="butterfly",time=datetime.time(minute=2,second=4),distance="200",user=user)


swimtimes12 = Swimtime(stroke="breaststroke",time=datetime.time(second=25),distance="50",user=user)
swimtimes13 = Swimtime(stroke="breaststroke",time=datetime.time(second=26),distance="50",user=user)
swimtimes14 = Swimtime(stroke="breaststroke",time=datetime.time(second=54),distance="100",user=user)
swimtimes15 = Swimtime(stroke="breaststroke",time=datetime.time(second=56),distance="100",user=user)
swimtimes16 = Swimtime(stroke="breaststroke",time=datetime.time(minute=2,second=15),distance="200",user=user)
swimtimes17= Swimtime(stroke="breaststroke",time=datetime.time(minute=2,second=4),distance="200",user=user)


swimtimes18 = Swimtime(stroke="backstroke",time=datetime.time(second=25),distance="50",user=user)
swimtimes19= Swimtime(stroke="backstroke",time=datetime.time(second=26),distance="50",user=user)
swimtimes20= Swimtime(stroke="backstroke",time=datetime.time(second=54),distance="100",user=user)
swimtimes21= Swimtime(stroke="backstroke",time=datetime.time(second=56),distance="100",user=user)
swimtimes22 = Swimtime(stroke="backstroke",time=datetime.time(minute=2,second=15),distance="200",user=user)
swimtimes23= Swimtime(stroke="backstroke",time=datetime.time(minute=2,second=4),distance="200",user=user)



session.add_all([swimtimes,swimtimes1,swimtimes2,swimtimes3,swimtimes4,swimtimes5,swimtimes6,swimtimes7,swimtimes8,swimtimes9,swimtimes10,swimtimes11,swimtimes12,swimtimes13,swimtimes14,swimtimes15,swimtimes16,swimtimes17,swimtimes18,swimtimes19,swimtimes20,swimtimes21,swimtimes22,swimtimes23])
session.commit()