const persons = [
	{
		person: "s",
		age: 2,
	},
	{
		person: "da",
		age: 3,
	},
	{
		person: "aw",
		age: 4,
	},
];

const res = persons.find(fl);

function fl(person) {
	return person.person === "s";
}

console.log(res);

res.age = 6;

console.log(persons);
