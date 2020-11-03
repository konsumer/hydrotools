import tarfile
import untangle
import os
import html2text

class Hydrogen:
  def __init__(self, filename, outdir):
    self.filename = filename
    self.outdir = outdir
    self.archive = tarfile.open(filename, "r")
    self.archive.extractall(outdir)
    for t in self.archive.getmembers():
      if os.path.basename(t.name) == 'drumkit.xml':
        self.xml = self.archive.extractfile(t).read().decode('utf8')
        self.doc = untangle.parse(self.xml)
        self.name = self.doc.drumkit_info.name.cdata
        self.author = self.doc.drumkit_info.author.cdata
        self.info = html2text.html2text(self.doc.drumkit_info.info.cdata).strip()
        self.dirname = os.path.dirname(t.name)
        self.instruments = []
        for i in self.doc.drumkit_info.instrumentList.instrument:
          instrument = {
            "region": int(i.id.cdata),
            "name": i.name.cdata,
            "volume": float(i.volume.cdata),
            "isMuted": bool(i.isMuted.cdata),
            "panL": float(i.pan_L.cdata),
            "panR": float(i.pan_R.cdata),
            "layers": []
          }
          
          try:
            # 1 file instruments don't have layers
            instrument["layers"].append({
              "min": 0.0,
              "max": 1.0,
              "gain": 1.0,
              "pitch": 0.0,
              "file": "%s/%s" % (self.dirname, i.filename.cdata)
            })
          except:
            for l in i.layer:
              instrument["layers"].append({
                "min": float(l.min.cdata),
                "max": float(l.max.cdata),
                "gain": float(l.gain.cdata),
                "pitch": float(l.pitch.cdata),
                "file": "%s/%s" % (self.dirname, l.filename.cdata)
              })
          
          self.instruments.append(instrument)

