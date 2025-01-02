const { Student } = require("../Models/StudentModel");

exports.getAllStudents = async (req, res) => {
  console.log("hello");
  try {
    console.log(Student);

    const students = await Student.find({});
    console.log(students);
    // Process students data here

    if (!students) {
      res.status(404).json({ error: "No students" });
    }
    console.log("student", students);
    res.json(students);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.getStudentById = async (req, res) => {
  try {
    const { id } = req.params;
    console.log(id);

    // Find the student by ID
    const student = await Student.find({ idNumber: id });
    console.log("heelo", student);
    // Check if the student exists
    if (!student) {
      return res.status(404).json({ error: "Student not found" });
    }
    console.log("heelo", student);
    res.json(student);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.deleteStudent = async (req, res) => {
  try {
    const { id } = req.params;

    // Check if the student exists

    const student = await Student.findOneAndDelete({ idNumber: id });

    if (!student) {
      return res.status(404).json({ error: "Student not found" });
    }

    // Delete the student

    res.json({ message: "Student deleted successfully" });
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.addStudent = async (req, res) => {
  try {
    const { name, idNumber, email, phoneNumber } = req.body;

    // Check if the student already exists by idNumber or email
    const existingStudent = await Student.findOne({
      $or: [{ idNumber: idNumber }, { email: email }],
    });

    if (existingStudent) {
      return res.status(400).json({ error: "Student already exists" });
    }

    const student = new Student({ name, idNumber, email, phoneNumber });
    const newStudent = await student.save();
    console.log(newStudent);
    res.json(newStudent);
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.updateStudent = async (req, res) => {
  try {
    const { id } = req.params;
    const { name, idNumber, email, phoneNumber } = req.body;
    console.log(name, idNumber, email, phoneNumber);
    // Check if the student exists
    const student = await Student.findOne({ idNumber: id });

    if (!student) {
      return res.status(404).json({ error: "Student not found" });
    }

    // Update the student details
    student.name = name;
    console.log(student.name);
    student.idNumber = idNumber;
    student.email = email;
    student.phoneNumber = phoneNumber;
    console.log(student);

    const updatedStudent = await student.save();

    res.json(updatedStudent);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.insertDummyData = (req, res) => {
  const dummyData = [
    {
      name: "khaled safi",
      idNumber: "2021001",
      email: "khaled.safi@admin.com",
      phoneNumber: "+970 76543210",
    },
    {
      name: "safi khaled",
      idNumber: "2021002",
      email: "safi.khaled@example.com",
      phoneNumber: "+970 76543211",
    },
    {
      name: "Robert Johnson",
      idNumber: "2021003",
      email: "robert.johnson@example.com",
      phoneNumber: "+970 35434535",
    },
    {
      name: "Emily Davis",
      idNumber: "2021004",
      email: "emily.davis@example.com",
      phoneNumber: "+970 35345335",
    },
    {
      name: "Michael Wilson",
      idNumber: "2021005",
      email: "michael.wilson@example.com",
      phoneNumber: "+970 3254542",
    },
    {
      name: "Olivia Taylor",
      idNumber: "2021006",
      email: "olivia.taylor@example.com",
      phoneNumber: "+970 4698854",
    },
    {
      name: "William Anderson",
      idNumber: "2021007",
      email: "william.anderson@example.com",
      phoneNumber: "+970  78678245",
    },
    {
      name: "Sophia Martinez",
      idNumber: "2021008",
      email: "sophia.martinez@example.com",
      phoneNumber: "+970 272452452",
    },
    {
      name: "Liam Thomas",
      idNumber: "2021009",
      email: "liam.thomas@example.com",
      phoneNumber: "+970 52734533",
    },
    {
      name: "Ava Clark",
      idNumber: "2021010",
      email: "ava.clark@example.com",
      phoneNumber: "+970 16785453",
    },
  ];

  Student.insertMany(dummyData)
    .then(function () {
      console.log("Successfully saved defult items to DB");
    })
    .catch(function (err) {
      console.log(err);
    });
};
